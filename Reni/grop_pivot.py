import pandas as pd
import matplotlib.pyplot as plt
#
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# excel_file = 'C:\\Users\\0487\\Desktop\\Омельяненко\\Рені\\РЕНІ.xlsx'
excel_file_2 = 'C:\\Users\\0487\\Desktop\\Омельяненко\\АНАЛІЗ_ЗП_філії\\Загальна_таблиця_ЗП.xlsx'
#
# # df=pd.read_excel(excel_file)
df2=pd.read_excel(excel_file_2)
# # print(df.info())
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

grouped = df2.groupby(['Філія','Посада (уніфікована)'])['Оплата простою'].sum().reset_index()
print(grouped)
# grouped = df.groupby(['Region', 'Product', 'Month'])['Sales'].sum().reset_index()

# Using pivot_table to reshape the data
pivot_table = grouped.pivot_table(index=['Посада (уніфікована)'], columns='Філія', values='Оплата простою', fill_value=0)

pivot_table.to_excel('pivot_table.xlsx', index=True)

plt.hist(pivot_table)
plt.show()

print("Pivot Table:")
