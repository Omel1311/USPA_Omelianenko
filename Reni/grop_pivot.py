import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
#
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

# excel_file = 'C:\\Users\\0487\\Desktop\\Омельяненко\\Рені\\РЕНІ.xlsx'
excel_file_2 = 'C:\\Users\\0487\\Desktop\\Омельяненко\\АНАЛІЗ_ЗП_філії\\Загальна_таблиця_ЗП.xlsx'
#
# # df=pd.read_excel(excel_file)
df2=pd.read_excel(excel_file_2)
print(df2.info())
# # print(df.memory_usage(deep=True))
# # print(df['ПП «Ларус Шиппінг» 2022'].value_counts()
#
# # print(df2.info())
# # ff = df2.iloc[0:4,6:11]
# # print(ff)
# print(df2.info())
#
#
# grouped2 = df2.groupby(['Філія','Посада (уніфікована)'])['Оплата простою'].agg('sum')
# print(grouped2)
#
# pivot2 = grouped2.pivot_table(index='Посада (уніфікована)', columns='Філія', values='Оплата простою', aggfunc='sum')
# print(pivot2.head())
#
# # print(df2.iloc[:,[2,4,11]].value_counts())
# import pandas as pd

# Sample purchase data
# Sample sales data


# Grouping by 'Region', 'Product', and 'Month', and calculating sum of 'Sales'

# # grouped = df2.groupby(['Філія','Посада (уніфікована)'])['Оплата простою'].sum().reset_index()
# grouped = df2.groupby(['Філія','Посада (уніфікована)'])['Оплата простою'].agg(sum).reset_index()
# print(grouped.sort_values(by='Оплата простою', ascending=False))
# # grouped = df.groupby(['Region', 'Product', 'Month'])['Sales'].sum().reset_index()
#
# # Using pivot_table to reshape the data
# pivot_table = grouped.pivot_table(index=['Посада (уніфікована)'], columns='Філія', values='Оплата простою', fill_value=0)
#
# pivot_table.to_excel('pivot_table.xlsx', index=True)
#
# grouped_2 = df2.groupby(['Найменування посади'])['Нараховано за посадовим окладом'].agg('mean', 'sum')
# print(type(grouped_2))
#
# print("Pivot Table:")
df2['Премії до свят'] = pd.to_numeric(df2['Премії до свят'], errors='coerce')
filtered_df = df2[(df2['ID']==1) | (df2['Філія'].str.contains('Чорн'))]
sorted = filtered_df.sort_values('Премії до свят', ascending=False)
# print(sorted)
# print(filtered_df)
# print(filtered_df.info())

df2['d']=pd.qcut(df2['ID'],q=4, labels=False)
print(df2)

df3 = df2.loc[df2['Нараховано за посадовим окладом']>100000, ['Філія','Найменування посади','Нараховано за посадовим окладом']]
print(df3.sort_values('Нараховано за посадовим окладом', ascending=False))
top = df3.nlargest(10, 'Нараховано за посадовим окладом')
print(top, 'Нараховано за посадовим окладом')
