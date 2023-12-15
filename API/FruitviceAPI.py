import requests
import json
import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

data = requests.get("https://fruityvice.com/api/fruit/all")
print(data.status_code)
results = json.loads(data.text)
print(results)
pd.DataFrame(results)
df2 = pd.json_normalize(results)
print(df2.head(50))

cherry = df2.loc[df2["name"] == 'Cherry']
print(cherry.head())
print((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus']))