import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sb

# url= "C:\\Users\\0487\\Desktop\\Омельяненко\\кпд\\зп.xlsx"
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
# df = pd.read_excel(url, sheet_name='Зведена_простій')
df = pd.read_csv(url, names=headers)
df.replace('?', np.NAN, inplace=True)
df[['price', 'horsepower']] = df[['price', 'horsepower']].astype(float)
df['price'] = df['price'].fillna(0)
print(df.info())


# coof, P_value = stats.pearsonr(df['prise'], df['year'])
# P_value1 = np.format_float_positional(P_value, trim='-')

# print('coof = ', coof, 'P_value = ', P_value1 )
df.to_excel('sea.xlsx')
sb.set (rc = {'figure.figsize':(8, 8)})
dataplot = sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
plt.show()

# s.to_excel('ddddd.xlsx')


# df_pivot = df.pivot(index='name', columns='year')
#
#
# df_pivot.to_excel('df_pivot.xlsx')