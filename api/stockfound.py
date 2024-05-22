from flask import jsonify, request, Blueprint
from flask_restful import Resource, Api
from datetime import datetime
from model.stockfind import Stockfind

# Create Flask blueprint for the new endpoint
stocks_found = Blueprint('stocks_found', __name__, url_prefix='/api/found')
api = Api(stocks_found)

class FoundingDateFilterResource(Resource):
    
    def __init__(self):
        self.model = Stockfind.get_instance()

    def post(self):
        try:
            payload = request.get_json()
            if 'dates' not in payload:
                return {'error': 'Dates not provided'}, 400

            # Convert date strings to years
            try:
                dates = [datetime.strptime(date, '%Y-%m-%d').year for date in payload['dates']]
            except ValueError as e:
                return {'error': f'Invalid date format: {str(e)}'}, 400

            # Get closest founding dates
            closest_dates = self.model.get_closest_founding_dates(dates)

            # Format the data as a list of dictionaries
            formatted_data = [
                {
                    'Company Name': entry['Company Name'],
                    'Founded': entry['Founded'],
                    'Difference': entry['Difference'],
                    'GICS Sector': entry['GICS Sector']  
                }
                for entry in closest_dates
            ]

            return formatted_data, 200

        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(FoundingDateFilterResource, '/filter')
