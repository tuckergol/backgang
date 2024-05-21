import pandas as pd

class Stockfind:
    _instance = None
    
    def __init__(self):
        self.data = pd.read_csv('S&P500.csv')
        self._clean()

    def _clean(self):
        self.data.drop(columns=['CIK', 'Date first added', 'Headquarter'], inplace=True)
        self.data['Sector'] = self.data['Sector'].apply(
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
        self.data['Founded'] = pd.to_numeric(self.data['Founded'], errors='coerce')

    def get_closest_founding_dates(self, dates):
        results = []
        for date in dates:
            self.data['Difference'] = abs(self.data['Founded'] - date)
            closest = self.data.loc[self.data['Difference'].idxmin()]
            results.append({
                'Company Name': closest['Name'],
                'Founded': int(closest['Founded']),
                'Difference': int(closest['Difference']),
                'Sector': closest['Sector']
            })
        return results

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

def initfind():
    Stockfind.get_instance()
