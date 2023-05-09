import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset_url = ('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df = pd.read_csv(dataset_url)
hardship_index = pd.read_sql_query()
pd.set_option('display.max.columns', None)
print(df.head())
df.plot(x='community_area_name', y='hardship_index', figsize=(7,5))
plt.show()