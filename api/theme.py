from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.users import User
from werkzeug.security import check_password_hash
from __init__ import db

settings_api = Blueprint('settings_api', __name__, url_prefix='/api/theme')
api = Api(settings_api)

class Username(Resource):
    def post(self):
        user_data = request.get_json()
        current_name = user_data.get('_name')
        user_uid = user_data.get('_uid')
        password = user_data.get('_password')
        new_name = user_data.get('new_name')

        if not all([current_name, user_uid, password, new_name]):
            return jsonify({'message': 'All fields are required'}), 400

        user = User.query.filter_by(_uid=user_uid).first()
        if user and user._name == current_name and check_password_hash(user._password, password):
            user._name = new_name
            db.session.commit()
            return jsonify({'message': 'Name updated successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials or user not found'}), 401

class UID(Resource):
    def post(self):
        user_data = request.get_json()
        current_name = user_data.get('_name')
        user_uid = user_data.get('_uid')
        password = user_data.get('_password')
        new_uid = user_data.get('new_uid')

        if not all([current_name, user_uid, password, new_uid]):
            return jsonify({'message': 'All fields are required'}), 400

        user = User.query.filter_by(_uid=user_uid).first()
        if user and user._name == current_name and check_password_hash(user._password, password):
            user._uid = new_uid
            db.session.commit()
            return jsonify({'message': 'User ID updated successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials or user not found'}), 401

api.add_resource(Username, '/change-name')
api.add_resource(UID, '/change-uid')
