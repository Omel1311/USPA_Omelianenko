import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl



pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

mpl.style.use('ggplot')  # optional: for ggplot-like style
#_______________________________________________________________
file_name ='C:\\Users\\0487\\Downloads\\Canada.csv'
df_can = pd.read_csv(file_name)
print(df_can.head())
print(df_can.shape)
#_______________________________________________________________
print('*'*8300)
df_can.set_index('Country', inplace=True)
print(df_can.head())
#_______________________________________________________________
years = list(map(str, range(1980, 2014)))
print(years)
#_______________________________________________________________
print('*'*8300)
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(3)

# transpose the dataframe
df_top5 = df_top5[years].transpose()

print(df_top5.head())
#_______________________________________________________________
# let's change the index values of df_top5 to type integer for plotting
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='area',alpha=0.45,
             stacked=False,
             figsize=(20, 10))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()