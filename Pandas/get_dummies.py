import pandas as pd
import numpy as np


url = 'C:\\Users\\0487\\Desktop\\ПО\\ІАБ_Портові оператори.xlsx'

df = pd.read_excel(url, sheet_name=0)

print(df.info())

missing_data = df.isnull()
# print('')
# for column in missing_data.columns.values.tolist():
#     print(column)
#     print(missing_data[column].value_counts())
#     print('*'*30)

ss = missing_data['Вид товару'].value_counts()


# print('max', df[['Вид товару']].value_counts().tolist())
df.dropna(subset=('Вид товару', 'Причали за договором'), axis=0, inplace=True)
df.drop(columns='№', inplace=True)

df['num-of-doors'] =  df['num-of-doors'].replace(np.NAN, df['num-of-doors'].idxmax(), inplace=True)

df['new'] =df['Участь в зерновій ініціативі'] + "_" + df['Спосіб доставки вантажу в порт']
df.drop(columns='new', inplace=True)
df.to_excel('C:\\Users\\0487\\Desktop\\ПО\\оператори.xlsx')

