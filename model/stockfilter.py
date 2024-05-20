import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
# Import the required libraries for the TitanicModel class
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


class Stocksort:
    _instance = None
    def __init__(self):
        self.data = pd.read_csv('S&P500.csv')
    def _clean(self):
        self.data.drop(columns=['CIK','Date added','Headquarters Location'],inplace=True)
        self.data['GICS Sector'] = self.data['GICS Sector'].apply(
            lambda x: 1 if x == 'Communication Services' else
                      2 if x == 'Consumer Discretionary' else
                      3 if x == 'Consumer Staples' else
                      4 if x == 'Energy' else 
                      5 if x == 'Financials' else
                      6 if x == 'Health Care' else
                      7 if x == 'Industrials' else
                      8 if x == 'Information Technology' else
                      9 if x == 'Materials' else 
                      10 if x == 'Real Estate' else
                      0
        )
    def _Jsonclean(self,payload):
        payload_df = pd.DataFrame(payload, index=[0])
        payload_df['GICS Sector'] = payload_df['GICS Sector'].apply(
            lambda x: 1 if x == 'Communication Services' else
                      2 if x == 'Consumer Discretionary' else
                      3 if x == 'Consumer Staples' else
                      4 if x == 'Energy' else 
                      5 if x == 'Financials' else
                      6 if x == 'Health Care' else
                      7 if x == 'Industrials' else
                      8 if x == 'Information Technology' else
                      9 if x == 'Materials' else 
                      10 if x == 'Real Estate' else
                      0
        )
        num = payload_df['GICS Sector'].tolist()
        return num
    @classmethod
    def get_instance(cls):
        """Gets, and conditionally cleans and builds, the singleton instance of the Food model."""
        if cls._instance is None:
            cls._instance = cls()
            cls._instance._clean()
        return cls._instance
def initstock():
    Stocksort.get_instance()


        
        