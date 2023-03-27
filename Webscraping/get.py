import requests
from bs4 import BeautifulSoup as BS

url = 'https://hometools.com.ua/g93995295-perforatory'

r = requests.get(url)

html = BS(r.content, 'lxml')


h2 = html.find_all(class_='cs-image-holder__image-link')
print(h2.text)

#for n, el in enumerate (h2):
    #print(n, el.text)

#NewProductTitle = html.find_all(class_= 'NewProductTitle')
#print(NewProductTitle)




