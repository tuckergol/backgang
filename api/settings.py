# imports
from flask import Blueprint, request, g
from flask_restful import Api, Resource
import base64
from model.users import User
from werkzeug.security import check_password_hash
from __init__ import db

# Setting up Blueprint for settings API
settings_api = Blueprint('settings_api', __name__, url_prefix='/api/settings')
api = Api(settings_api)

# Resource: username-changing
class ChangeUsername(Resource):
    def put(self):
        # Get JSON data from request body
        body = request.get_json()
        current_name = body.get('_name')
        user_uid = body.get('_uid')
        password = body.get('_password')
        new_name = body.get('new_name')

        # Check if all required fields provided
        if not all([current_name, user_uid, password, new_name]):
            return {'message': 'All fields are required'}, 400

        # Query database to find user by UID
        user = User.query.filter_by(_uid=user_uid).first()
        # Verify that user exists & if password is correct
        if user and user._name == current_name and check_password_hash(user._password, password):
            user._name = new_name  # Update username
            db.session.commit()  # Commit changes to database
            return {'message': 'Name updated successfully'}, 200
        else:
            return {'message': 'Invalid credentials or user not found'}, 404

# Resource: uploading profile picture/image
class UploadProfilePicture(Resource):
    def post(self):
        # Check if file part is in request
        if 'file' not in request.files:
            return {'message': 'Please upload an image first'}, 400
        file = request.files['file'] # Retrieve file from request
        # Ensure file selected for upload
        if file.filename == '':
            return {'message': 'No selected file'}, 400
        
        user_uid = request.form.get('uid') # get user UID from form data
        user = User.query.filter_by(_uid=user_uid).first() # Find user by UID
        if user:
            # File conversion/reading (seen below) was co-developed with ChatGPT
            img_data = file.read()  # Read image data from provided/inputted file
            base64_encoded = base64.b64encode(img_data).decode('utf-8')  # Encode image data as base64
            user._pfp = base64_encoded  # Update profile picture data
            db.session.commit()  # Commit changes to database
            return {'message': 'Profile picture updated successfully'}, 200
        else:
            return {'message': 'User not found'}, 404

class GetUsername(Resource):
    def get(self):
        user_uid = request.args.get('uid')
        
        if not user_uid:
            return {'message': 'UID required. Please sign in.'}, 400
        
        user = User.query.filter_by(_uid=user_uid).first()
        
        if user:
            user_data = {
                'name': user._name,
            }
            return user_data, 200
        else:
            return {'message': 'User not found'}, 404
        
class GetProfilePicture(Resource):
    def get(self):
        user_uid = request.args.get('uid')

        if not user_uid:
            return {'message': 'UID is required. Please sign in.'}, 400

        user = User.query.filter_by(_uid=user_uid).first()

        if user and user._pfp:
            return {'pfp': user._pfp}, 200

# Register API resources with routes
api.add_resource(ChangeUsername, '/change-name')
api.add_resource(UploadProfilePicture, '/profile-picture')
api.add_resource(GetUsername, '/get-user-name')
api.add_resource(GetProfilePicture, '/get-profile-picture')