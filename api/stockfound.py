from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pandas as pd
from model.stockfilter import Stocksort
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from flask_restful import Resource
from flask import Blueprint, jsonify, request 
from flask_restful import Api, Resource
from datetime import datetime

stocks_found = Blueprint('stocks_found', __name__, url_prefix='/api/found')
api = Api(stocks_found)

class FoundingDateFilterResource(Resource):
    
    def __init__(self):
        self.model = Stocksort.get_instance()

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