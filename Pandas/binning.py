import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sb



# url= "C:\\Users\\0487\\Desktop\\Омельяненко\\кпд\\вердиш\\загальний.xlsx"
url= 'C:\\Users\\0487\\Desktop\\Омельяненко\\кпд\\зп.xlsx'
df = pd.read_excel(url, sheet_name='python_2')
print(df.info())
df.fillna(0)
# print(df.info())
# df_test = df[['Показник','2022 Ізмаїльський морський порт', '2022 Ренійський морський порт', '2022 Морський порт "Усть-Дунайськ"', 'дата']]

# df_test_group = df_test.groupby(['дата','2022 Ренійський морський порт', 'Показник'], as_index=False).mean()
# df_pivot = df_test_group.pivot(index='дата', columns='Показник')
# pears_c, p = stats.pearsonr(df['2022 Ізмаїльський морський порт'], df['2022 Ренійський морський порт'])
# df_pivot.to_excel('pivot.xlsx')
# # des = df.describe()
# df_test_group.to_excel('df.xlsx')


#
# scatter1 = df.plot.scatter(x='Штат', y='Фінансовий_результат', c='Фінансовий_результат', colormap='viridis')
# plt.show()
#
# # df[['Не в протсої на ставку 100%остої на 0,75 ставки', 'Не в простої на 0,5 ставки']].plot.hist()
# # plt.title('Test1')
# # plt.xlabel('numbers')
# plt.ylabel('frequency')
# plt.show()

# df.columns = headers
#
# df = df.replace('?', np.NAN)
# #pd.set_option('display.max_columns', 10)
#
#
# print('*'*30)
# df['city-mpg'] = 235/df['city-mpg']
#
#
# #  print(df[['length']].head())
# df.rename(columns={'city-mpg':'city-L/100km'}, inplace=True)
#
# df['length'] = (df['length']-df['length'].mean())/df['length'].std()
# #  print(df[['length']].head())
#
# df['price'] = df['price'].astype('float')
# bins = np.linspace(min(df['price']),max(df['price']),4)
# print(bins)
#
# group = ['low','mid', 'high']
#
# df['binning'] = pd.cut(df['price'], bins, labels=group, include_lowest=True )
#
# print(df.head())
# print(df.dtypes)
#
#
#
#
# df['price']=df['price'].astype('float')
#
# # print(df['price'].describe())
# # z = (13900-13205)/7966
# # print('z=', round(z,4))
# # sc = 13205/45400
# # print('simple_scaling=', sc)
# # min_max = ((13205-5118)/(45400-5118))
# # print('min_max=', min_max)



# df.plot.scatter(x='length', y='price')
#
# plt.show()

# df.plot.hist()
# plt.show()
#
#
#
#
# print(pd.get_dummies(df['fuel-type'], dtype=int))
# print(df.head())

print(df.dtypes)
df22 = df[['Підрозділ', 'Штат', 'Середня_ЗП', 'Фінансовий_результат']]
df22 = df22.groupby(['Підрозділ'],as_index=False).mean()
df22.to_excel('df22.xlsx')


df33=pd.pivot_table(df, values='Штат', index='Дата', columns='Підрозділ')
df33.to_excel('df33.xlsx')




c,p = stats.pearsonr(df.where(filter,inplace=True)['Штат'], df['Фонд_ЗП'])
p1 = np.format_float_positional(p, trim='-')
print(p1, c)