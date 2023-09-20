import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

#_______________________________________________________________
# x = np.random.randn(1000)
# plt.plot(33,100,'o')
# plt.savefig('matplotlib.png')
# plt.show()
#_______________________________________________________________
file_name ='C:\\Users\\0487\\Downloads\\Canada.xlsx'
df = pd.read_excel(file_name, sheet_name="Canada by Citizenship", skiprows=range(20),
    skipfooter=2)
print(df.head())
print(df.info(verbose=False))
print(df.shape)
#_______________________________________________________________
df.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df.head(2))
#_______________________________________________________________

df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
#_______________________________________________________________
df['Total'] = df.sum(axis=1)
print(df['Total'])
#_______________________________________________________________
print(df.isnull().sum())
#_______________________________________________________________
df.set_index('Country', inplace=True)


print(df.loc['Haiti', 2000])
print(df.loc['Haiti', [1990, 1991, 1992, 1993, 1994, 1995]])


df.columns = list(map(str, df.columns))
year = list(map(str, range(1989, 2013)))
haiti = df.loc['Haiti', year]  # passing in years 1990 - 2013
print(haiti)

#_______________________________________________________________
condition = df['Continent'] == 'Asia'
q=df[(df['Continent'] == 'Asia') & (df['Region'] == 'South-Eastern Asia')]
print(q)

#_______________________________________________________________
