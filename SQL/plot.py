import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset_url = ('C:\\Users\\0487\\Desktop\\22222.csv')
df = pd.read_csv(dataset_url)

print(df.head())
df.plot(x='Indicator', y='Total by sea ports %', figsize=(7,5))
plt.show()