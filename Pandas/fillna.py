import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

url= "C:\\Users\\0487\\Desktop\\Омельяненко\\кпд\\вердиш\\загальний.xlsx"

df = pd.read_excel(url, sheet_name='python')

df_port = df[['2022 Ренійський морський порт', '2022 Ізмаїльський морський порт', '2022 Морський порт "Усть-Дунайськ"']].fillna(0)

df_port.to_excel('df_port.xlsx')

coof, P_value = stats.pearsonr(df_port['2022 Ренійський морський порт'], df_port['2022 Ізмаїльський морський порт'])

print(coof, P_value)