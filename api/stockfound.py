from flask import Flask, jsonify, request, Blueprint
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
                return jsonify({'error': 'Dates not provided'})

            dates = [datetime.strptime(date, '%Y-%m-%d').year for date in payload['dates']]
            closest_dates = self.model.get_closest_founding_dates(dates)
            return jsonify(closest_dates)

        except Exception as e:
            return jsonify({'error': str(e)})

api.add_resource(FoundingDateFilterResource, '/filter')
