import pandas as pd
import numpy as np


url = 'C:\\Users\\0487\\Desktop\\ПО\\ІАБ_Портові оператори.xlsx'

df = pd.read_excel(url, sheet_name=0)

print(df.info())

print(df[['Вид товару']])

d = pd.get_dummies(df)

d.to_excel('s.xlsx')