from flask import jsonify, request, Blueprint  # Import necessary Flask modules
from flask_restful import Resource, Api  # Import Flask-RESTful modules for building REST APIs
from datetime import datetime  # Import datetime for date manipulation
from model.stockfind import Stockfind  # Import the Stockfind class from the model

# Create Flask blueprint for the new endpoint
stocks_found = Blueprint('stocks_found', __name__, url_prefix='/api/found')
api = Api(stocks_found)  # Initialize the API with the blueprint

class FoundingDateFilterResource(Resource):
    
    def __init__(self):
        self.model = Stockfind.get_instance()  # Get the singleton instance of Stockfind

    def post(self):
        try:
            payload = request.get_json()  # Get JSON payload from the POST request
            if 'dates' not in payload:
                return {'error': 'Dates not provided'}, 400  # Return error if 'dates' is not in the payload

            # Convert date strings to years
            try:
                dates = [datetime.strptime(date, '%Y-%m-%d').year for date in payload['dates']]
            except ValueError as e:
                return {'error': f'Invalid date format: {str(e)}'}, 400  # Return error if date format is invalid

            # Get closest founding dates using the Stockfind model
            closest_dates = self.model.get_closest_founding_dates(dates)

            # Format the data as a list of dictionaries
            formatted_data = [
                {
                    'Company Name': entry['Company Name'],
                    'Founded': entry['Founded'],
                    'Difference': entry['Difference'],
                    'GICS Sector': entry['GICS Sector']
                }
                for entry in closest_dates  # Iterate over the closest dates to format each entry
            ]

            return formatted_data, 200  # Return the formatted data with a 200 OK status

        except Exception as e:
            return {'error': str(e)}, 500  # Return a generic error if an exception occurs

# Add the resource to the API, specifying the endpoint
api.add_resource(FoundingDateFilterResource, '/filter')
