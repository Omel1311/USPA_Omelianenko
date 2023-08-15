import pandas as pd
import re
excel_file = 'C:\\Users\\0487\\Desktop\\Омельяненко\\АНАЛІЗ_ЗП_філії\\POWER_ZP.xlsx'

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

df = pd.read_excel(excel_file)

df['Премії до свят'] = df['Премії до свят'].replace('-','')
print(df.info())
df['Премії до свят'] =df['Премії до свят'] = pd.to_numeric(df['Премії до свят'], errors='coerce')
# df.to_csv('General_ZP.uk.en.csv')
# df['Премії до свят']= df.astype({'Премії до свят': float})
print(df.info())
# df = pd.read_excel(excel_file, sheet_name=None)
# for key in df.keys():
#    df[key].to_csv('{}.csv'.format(key))
