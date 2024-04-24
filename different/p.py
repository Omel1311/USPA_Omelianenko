import pandas as pd


df = pd.read_excel('C:\\Users\\0487\\Desktop\\33.xlsx')

# df_transposed = df.T

df_cleaned =df[~df.isin([2023]).any(axis=1)]

df_final = df_cleaned.dropna()

df_transposed1 = df_final.to_excel("333.xlsx")
print(df_final.head())

