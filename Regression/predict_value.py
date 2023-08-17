import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression



pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)


excel_file = 'C:\\Users\\0487\\Desktop\\Омельяненко\\АНАЛІЗ_ЗП_філії\\Загальна_таблиця_ЗП.xlsx'

df=pd.read_excel(excel_file)

model = LinearRegression()

df = df.fillna(0)
print(df.tail(30))

X= df[['Нараховано всього', 'Квартальна премія']]
y=df['Нараховано за посадовим окладом']

model.fit(X,y)

new_x = pd.DataFrame({'Нараховано всього': [10000], 'Квартальна премія':[4444]})
Y_predict = model.predict(new_x)
print(Y_predict)


