from auth_middleware import token_required
import jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource
from model.users import User
from __init__ import db
from model.themes import initTheme  # Importing initTheme from themes.py

theme_api = Blueprint('theme_api', __name__, url_prefix='/api/users')
api = Api(theme_api)

class _Settings(Resource):
    def put(self):
        data = request.json.get('settings')
        uid = data.get('uid')
        username = data.get('name')
        password = data.get('password')
        theme = data.get('theme')

        user = User.query.filter_by(_uid=uid).first()
        print(user)
        if user is None or not user.is_password(password) or user.name != username:
            return {'error': 'Invalid user credentials or theme'}, 400
        
        if theme not in ['light', 'dark']:
            return {'error': 'Invalid theme specified'}, 400
        
        user.theme = theme
        db.session.commit()

        return {'message': 'Settings saved successfully'}, 200

api.add_resource(_Settings, '/save_settings')