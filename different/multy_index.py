import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
# arrays = [
#     ['Фінанси', 'Фінанси', 'Продажі', 'Продажі'],
#     ['Доходи', 'Витрати', 'Доходи', 'Витрати']
# ]
#
# multi_index = pd.MultiIndex.from_arrays(arrays, names=['Розділ', 'Показник'])
#
# data = [[100, 50, 200, 120]]
# df = pd.DataFrame(data, columns=multi_index)
#
# print(df)

df = pd.read_excel("C:\\Users\\0487\\Downloads\\KI.xlsx", sheet_name='2026', header=[0, 1, 2])

df.columns = ['indicator_nameі', 'total',
              'loan_imf', 'loan_state', 'loan_banks', 'loan_total',
              'budget_funds',
              'own_amortization', 'own_profit', 'own_total',
              'other_sources',
              'branch_unit', 'department_name', 'object_group']

df.to_csv("C:\\Users\\0487\\Desktop\\KI_clean2.csv", index=False, encoding='utf-8-sig')

df.to_excel("KI_cleanexxx.xlsx", index=False)

print(df.head(10))