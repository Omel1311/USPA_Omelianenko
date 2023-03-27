import pandas as pd
import requests
from bs4 import BeautifulSoup

#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
data = requests.get(url).text

#soup = BeautifulSoup(data, 'html5lib')
#print(soup.text)
read_html_pandas_data = pd.read_html(url)
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.to_excel('crypto_stock.xlsx')
print(netflix_dataframe.head())