import pandas as pd
import numpy as np

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(url, names=headers)
print(df['num-of-doors'].head())
df.replace('?', np.NAN, inplace=True

print(df['num-of-doors'].head())
max_doors = df['num-of-doors'].value_counts().idxmax()
print('max_doors: ', max_doors)
df['num-of-doors'].replace(np.NAN, max_doors, inplace=True)
print(df['num-of-doors'].head())

# missing_data = df.isnull()
# print(missing_data.head())
#
# for column in missing_data.columns.values.tolist():
#     print(column)
#     print (missing_data[column].value_counts())
#     print("")
#
# print(df['normalized-losses'].astype(float).idxmax())
#
# print('missing data', missing_data['price'].value_counts())
# print(df['price'].value_counts())

df.to_excel('C:\\Users\\0487\\Desktop\\Омельяненко\\Data Science\\авто2.xlsx', sheet_name='auto_2')