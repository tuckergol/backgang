import pandas as pd
import re

class Stockfind:
    _instance = None  # Class-level variable to hold the singleton instance

    def __init__(self):
        self.data = pd.read_csv('S&P500.csv')  # Read CSV file containing S&P 500 data
        self._clean()  # Clean the data after loading

    def _clean(self):
        # Retain only the necessary columns
        required_columns = ['Symbol', 'Founded', 'GICS Sector']
        # Ensure columns exist in the CSV
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Column {col} not found in the CSV file")

        self.data = self.data[required_columns]  # Keep only the required columns
        
        # Extract earliest year if the 'Founded' field contains multiple years
        self.data['Founded'] = self.data['Founded'].apply(lambda x: int(re.search(r'\d{4}', str(x)).group(0)))
        # Convert 'Founded' column to numeric, invalid parsing will be set as NaN
        self.data['Founded'] = pd.to_numeric(self.data['Founded'], errors='coerce')

    def merge_sort(self, arr):
        # Recursive merge sort implementation to sort the array of dictionaries by 'Founded' key
        if len(arr) > 1:
            mid = len(arr) // 2  # Find the middle of the array
            left_half = arr[:mid]  # Split the array into left half
            right_half = arr[mid:]  # Split the array into right half

            self.merge_sort(left_half)  # Recursively sort the left half
            self.merge_sort(right_half)  # Recursively sort the right half

            i = j = k = 0  # Initialize indices for left half, right half, and main array
            # Merge the sorted halves back into the main array
            while i < len(left_half) and j < len(right_half):
                if left_half[i]['Founded'] < right_half[j]['Founded']:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Copy any remaining elements from the left half
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Copy any remaining elements from the right half
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def get_companies_by_date_range(self, start_year, end_year):
        # Filter the data to get companies founded within the specified date range
        filtered_data = self.data[(self.data['Founded'] >= start_year) & (self.data['Founded'] <= end_year)]
        data_list = filtered_data.to_dict('records')
        self.merge_sort(data_list)  # Sort the list using merge sort
        return data_list

    @classmethod
    def get_instance(cls):
        # Implement the singleton pattern to ensure only one instance of Stockfind
        if cls._instance is None:
            cls._instance = cls()  # Create the instance if it does not exist
        return cls._instance  # Return the singleton instance

def initfind():
    # Initialize the Stockfind singleton instance
    Stockfind.get_instance()