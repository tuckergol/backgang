import pandas as pd
import re

class Stockfind:
    _instance = None
    
    def __init__(self):
        self.data = pd.read_csv('S&P500.csv')
        self._clean()

    def _clean(self):
        # Retain only the necessary columns
        required_columns = ['Symbol', 'Founded', 'GICS Sector']
        # Ensure columns exist in the CSV
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Column {col} not found in the CSV file")

        self.data = self.data[required_columns]
        
        # Extract earliest year if the 'Founded' field contains multiple years
        self.data['Founded'] = self.data['Founded'].apply(lambda x: int(re.search(r'\d{4}', str(x)).group(0)))
        self.data['Founded'] = pd.to_numeric(self.data['Founded'], errors='coerce')

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i]['Difference'] < right_half[j]['Difference']:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def get_closest_founding_dates(self, dates):
        results = []
        for date in dates:
            self.data['Difference'] = abs(self.data['Founded'] - date)
            data_list = self.data.to_dict('records')
            self.merge_sort(data_list)

            closest = data_list[0]
            results.append({
                'Company Name': closest['Symbol'],
                'Founded': int(closest['Founded']),
                'Difference': int(closest['Difference']),
                'GICS Sector': closest['GICS Sector']
            })
        return results

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

def initfind():
    Stockfind.get_instance()

