from flask import Blueprint, request
from flask_restful import Api, Resource
from model.users import User
from werkzeug.security import check_password_hash
from __init__ import db

settings_api = Blueprint('settings_api', __name__, url_prefix='/api/settings')
api = Api(settings_api)

class _ChangeUsername(Resource):
    def put(self):
        body = request.get_json()
        current_name = body.get('_name')
        user_uid = body.get('_uid')
        password = body.get('_password')
        new_name = body.get('new_name')

        if not all([current_name, user_uid, password, new_name]):
            return {'message': 'All fields are required'}, 400

        user = User.query.filter_by(_uid=user_uid).first()
        if user and user._name == current_name and check_password_hash(user._password, password):
            user._name = new_name
            db.session.commit()
            return {'message': 'Name updated successfully'}, 200
        else:
            return {'message': 'Invalid credentials: user not found'}, 404
    
class _ChangeUID(Resource):
    def put(self):
        body = request.get_json()
        current_name = body.get('_name')
        user_uid = body.get('_uid')
        password = body.get('_password')
        new_uid = body.get('new_uid')

        if not all([current_name, user_uid, password, new_uid]):
            return {'message': 'All fields are required'}, 400

        user = User.query.filter_by(_uid=user_uid).first()
        if user and user._name == current_name and check_password_hash(user._password, password):
            user._uid = new_uid
            db.session.commit()
            return {'message': 'User ID updated successfully'}, 200
        else:
            return {'message': 'Invalid credentials: user not found'}, 404

api.add_resource(_ChangeUsername, '/change-name')
api.add_resource(_ChangeUID, '/change-uid')
