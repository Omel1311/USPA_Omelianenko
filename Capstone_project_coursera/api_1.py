import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage with the table
url = "https://www.uspa.gov.ua/project/zvit-zerno"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table on the webpage (you may need to inspect the page source to identify the table's structure)
    table = soup.find('table')

    # Read the HTML table into a DataFrame using Pandas
    df = pd.read_html(str(table))[0]  # Use [0] to select the first table if there are multiple tables on the page

    # Now you have the table data in a Pandas DataFrame and can work with it
    # You can save it to a CSV file, display it, or perform further data analysis

    # For example, to save it to a CSV file:
    df.to_csv('uspa_zvit_zerno.csv', index=False)

    print("Table data scraped and saved to uspa_zvit_zerno.csv")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
