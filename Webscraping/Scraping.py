from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

url = "http://www.ibm.com"

data  = requests.get(url).text


soup = BeautifulSoup(data,"html.parser")

#for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    #print(link.get('href'))

for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))