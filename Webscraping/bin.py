import requests
import os
url='https://en.wikipedia.org/wiki/Silva_Method'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)