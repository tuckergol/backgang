from auth_middleware import token_required
import jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource
from model.themes import Theme
from __init__ import db

theme_api = Blueprint('theme_api', __name__, url_prefix='/api/theme')
api = Api(theme_api)

class UserAPI:
    class _Name(Resource):
        def get(self):
            name_data = Theme.query.with_entities(Theme._name).all()
            json_ready = [row[0] for row in name_data]
            print(json_ready)
            return jsonify(json_ready)
        def put(self):
            body = request.get_json()
            uid = body.get('uid')
            new_name = body.get('new_name')

            # Check if the user exists
            user = Theme.query.filter_by(_uid=uid).first()
            if not user:
                return {'error': 'User not found'}, 404

            # Update the user's name
            user._name = new_name
            db.session.commit()

            return {'message': 'Username updated successfully'}, 200

    class _Settings(Resource):
        def post(self):
            data = request.json.get('settings')
            uid = data.get('uid')
            username = data.get('name')
            password = data.get('password')
            theme = data.get('theme')

            # Check if the provided user credentials match an existing user in the database
            user = Theme.query.filter_by(_uid=uid).first()
            print(user)
            if user is None or not user.is_password(password) or user.name != username:
                return {'error': 'Invalid user credentials or theme'}, 400
            
            # Check if the theme is 'light' or 'dark'
            if theme not in ['light', 'dark']:
                return {'error': 'Invalid theme specified'}, 400
            
            # Update the user's theme setting
            user.theme = theme
            db.session.commit()

            return {'message': 'Settings saved successfully'}, 200

    api.add_resource(_Name, '/name')
    api.add_resource(_Settings, '/save_settings')
