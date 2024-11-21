import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

df = pd.read_csv('C:\\Users\\0487\\Downloads\\w6.csv')
df.to_excel('w6.xlsx', index=False)


print(df.head(3))




