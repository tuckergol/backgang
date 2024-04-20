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
            if new_theme in ['light', 'dark']:
                user.theme = new_theme
                db.session.commit()
                return jsonify({'message': 'Theme updated successfully!'}), 200
            else:
                return jsonify({'message': 'Invalid theme choice'}), 400
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

api.add_resource(UpdateTheme, '/update')
api.add_resource(GetTheme, '/get-theme')
