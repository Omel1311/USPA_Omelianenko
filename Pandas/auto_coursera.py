import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sb

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'

df = pd.read_csv(url)
df.replace('?', np.NAN, inplace=True)
# df.to_excel('auto2.xlsx')
print(df.dtypes)

# dataplot = sb.heatmap(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr(), cmap="YlGnBu", annot=True)
# plt.show()

# colour as variables
# scatter1 = df.plot.scatter(x= 'stroke', y= 'price', c='price', colormap='viridis')
# plt.show()

# # regplot
# sb.regplot(x= 'highway-mpg', y= 'price', data=df)
# plt.ylim(0,)
#
# #  boxplot
# sb.boxplot(x= 'body-style', y= 'price', data=df)
# plt.ylim(0,)
# plt.show()

df2 = df['drive-wheels'].value_counts().to_frame()
df2.rename(columns={'drive-wheels': 'testq'}, inplace=True)
df2.index.name = "dss"
print(df2.head())

# df2.to_excel('df2.xlsx')

df3 = df['make'].value_counts().to_frame()
df3.rename(columns={'make': 'count'}, inplace=True)
df3.index.name = 'model'
# df3.to_excel('df3.xlsx')

df5 = pd.pivot_table(df, index=['make'], columns=['num-of-doors'], values='price', fill_value='&')
df5.rename(columns={'make':'model'}, inplace=True)
# df5.to_excel('df5.xlsx')

print(df['wheel-base'].unique())


df_group_one = df[['drive-wheels','body-style','price']]
df_group_one = df_group_one.groupby(['drive-wheels', 'body-style'],as_index=False).mean()
# df_group_one.to_excel('df5.xlsx')

group_pivot = pd.pivot_table(df_group_one, index='drive-wheels', columns='body-style')
# group_pivot.to_excel('df6.xlsx')



# sb.boxplot(x= 'drive-wheels', y= 'price', data=df)

# scatter1 = df.plot.scatter(x= 'drive-wheels', y= 'price', c='price', colormap='viridis')
# plt.ylim(0,)
# plt.show()

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)