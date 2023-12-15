import requests
import json
import pandas as pd
import requests

import requests

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

api_url = "https://fruityvice.com/api/fruit/all"

def display_number_of_fruits(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors

        if response.ok:
            data = response.json()

            # Uncomment the line below to print the entire API response
            print(json.dumps(data, indent=2))

            # Create a dictionary to store the count of each family
            family_counts = {}

            for fruit in data:
                family = fruit.get('family', 'Unknown')

                # If the family is not already in the dictionary, add it with a count of 1
                if family not in family_counts:
                    family_counts[family] = 1
                else:
                    family_counts[family] += 1

            # Print the count for each family
            for family, count in family_counts.items():
                print(f"Number of fruits in the {family} family: {count}")
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")

# Example usage:
display_number_of_fruits(api_url)


