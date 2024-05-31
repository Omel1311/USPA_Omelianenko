import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df = pd.read_csv("C://Users//0487//Downloads//CarPrice_Assignment.csv")

print(df.head())

# missing_data = df.isnull()
# print('')
# for column in missing_data.columns.values.tolist():
#     print(column)
#     print(missing_data[column].value_counts())
#     print('*'*30)


filtered_values = df[df['curbweight'] > 3000][['curbweight', 'price']].sort_values(by='price', ascending=False)
print(filtered_values)

group = df.groupby('fueltype')['price'].mean()
print(group.head())
