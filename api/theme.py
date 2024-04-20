from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.users import User
from werkzeug.security import check_password_hash
from __init__ import db

theme_api = Blueprint('theme_api', __name__, url_prefix='/api/theme')
api = Api(theme_api)

class UpdateTheme(Resource):
    def post(self):
        user_data = request.get_json()
        username = user_data.get('_name', '')
        user_uid = user_data.get('_uid', '')
        password = user_data.get('_password', '')
        new_theme = user_data.get('_theme', '')

        if not all([username, user_uid, password, new_theme]):
            return jsonify({'message': 'All fields are required'}), 400

        user = User.query.filter_by(_uid=user_uid).first()
        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        if user._name == username and check_password_hash(user._password, password):
            user._theme = new_theme
            db.session.commit()
            return jsonify({'message': 'Theme updated successfully'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

class GetTheme(Resource):
    def get(self):
        uid = request.args.get('uid')
        user = User.query.filter_by(_uid=uid).first()
        if user:
            return jsonify({'theme': user.theme}), 200
        else:
            return jsonify({'message': 'User not found'}), 404

class ChangeUserName(Resource):
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

api.add_resource(UpdateTheme, '/update')
api.add_resource(GetTheme, '/get-theme')
api.add_resource(ChangeUserName, '/change-name')
