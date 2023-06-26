import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

url= "C:\\Users\\0487\\Desktop\\Омельяненко\\кпд\\зп.xlsx"

df = pd.read_excel(url, sheet_name='python_2')
print(df.info())
coof, P_value = stats.pearsonr(df['Фонд ЗП'], df['Штат'])
print('coof = ', coof, 'P_value = ', P_value )