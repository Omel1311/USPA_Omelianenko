import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import seaborn as sns

#_______________________________________________________________
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
#_______________________________________________________________
mpl.style.use('ggplot') # optional: for ggplot-like style
#_______________________________________________________________

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
# print(df_can.head())
#_______________________________________________________________

print(df_can.shape)
df_can.set_index('Country', inplace=True)
#_______________________________________________________________

sns.countplot(x='Continent', data=df_can)


# ___________________________________________________
# Barplot
df_Can2 = df_can.groupby('Continent')['Total'].mean()
print(df_Can2)

df_Can3 = df_can.groupby('Continent')['Total'].sum()
print(df_Can3)

plt.figure(figsize=(15, 10))
sns.barplot(x='Continent', y='Total', data=df_can)
plt.show()
#_______________________________________________________________
# Regression Plot
years = list(map(str, range(1980, 2014)))
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
plt.figure(figsize=(15, 10))

sns.set(font_scale=1.5)

ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()


# change background to white background
# plt.figure(figsize=(15, 10))
#
# sns.set(font_scale=1.5)
# sns.set_style('ticks')  # change background to white background
#
# ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
# ax.set(xlabel='Year', ylabel='Total Immigration')
# ax.set_title('Total Immigration to Canada from 1980 - 2013')
# plt.show()