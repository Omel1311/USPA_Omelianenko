import requests
import json
import pandas as pd
import os
from PIL import Image
from IPython.display import IFrame

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

data = requests.get("https://www.uspa.gov.ua/wp-content/uploads/2023/06/a2ac0336-6dd5-4266-84fe-13eab652d1e4-400x250.jpg")
print(data.status_code)
print(data.request.headers)

print("request body:", data.request.body)

header=data.headers
print(data.headers)
print(header['date'])
print(data.text[0:500])

path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(data.content)
Image.open(path)