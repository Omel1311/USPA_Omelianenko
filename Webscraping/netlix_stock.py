import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

#First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link.get('src'))

for row in soup.find("tbody").find_all('tr'):

    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

# Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data, pd.DataFrame({
        "Date": [date],
        "Open": [Open],
        "High": [high],
        "Low": [low],
        "Close": [close],
        "Adj Close": [adj_close],
        "Volume": [volume]
    })], ignore_index=True)

print(netflix_data.head())

