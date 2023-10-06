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


