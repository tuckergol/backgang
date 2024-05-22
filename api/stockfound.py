from flask import jsonify, request, Blueprint
from flask_restful import Resource, Api
from datetime import datetime
from model.stockfind import Stockfind

# Create Flask blueprint for the new endpoint
stocks_found = Blueprint('stocks_found', __name__, url_prefix='/api/found')
api = Api(stocks_found)  # Initialize the API with the blueprint

class FoundingDateFilterResource(Resource):

    def __init__(self):
        self.model = Stockfind.get_instance()  # Get the singleton instance of Stockfind

    def post(self):
        try:
            payload = request.get_json()  # Get JSON payload from the POST request
            if 'dates' not in payload or len(payload['dates']) != 2:
                return {'error': 'Start and end dates not provided'}, 400  # Return error if 'dates' are not in the payload

            # Convert date strings to years
            try:
                start_date = datetime.strptime(payload['dates'][0], '%Y-%m-%d').year
                end_date = datetime.strptime(payload['dates'][1], '%Y-%m-%d').year
            except ValueError as e:
                return {'error': f'Invalid date format: {str(e)}'}, 400  # Return error if date format is invalid

            # Get companies founded within the date range using the Stockfind model
            filtered_data = self.model.get_companies_by_date_range(start_date, end_date)

            # Format the data as a list of dictionaries
            formatted_data = [
                {
                    'Company Name': entry['Symbol'],
                    'Founded': entry['Founded'],
                    'GICS Sector': entry['GICS Sector']
                }
                for entry in filtered_data  # Iterate over the filtered data to format each entry
            ]

            return formatted_data, 200  # Return the formatted data with a 200 OK status

        except Exception as e:
            return {'error': str(e)}, 500  # Return a generic error if an exception occurs

# Add the resource to the API, specifying the endpoint
api.add_resource(FoundingDateFilterResource, '/filter')
