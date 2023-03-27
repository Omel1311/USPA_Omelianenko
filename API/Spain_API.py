import requests
import json
import pandas as pd

data = requests.get('https://tenders.guru/api/es/tenders/{}')
results  = json.loads(data.text)
df = pd.DataFrame(results)
print(df)

df2 = df.to_excel('Spain_Procurement_API.xlsx')