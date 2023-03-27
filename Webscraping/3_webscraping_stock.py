import pandas as pd
import requests
from bs4 import BeautifulSoup

#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
data = requests.get(url).text

html_data = BeautifulSoup(data, 'html5lib')
title = html_data.find('title')
print(title)
print(html_data.find_all('title'))


