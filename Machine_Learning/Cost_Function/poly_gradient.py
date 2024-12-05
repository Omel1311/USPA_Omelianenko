import pandas as pd
from Polynomial_function import PlotPolyReg

# Создаем пример данных
df = pd.read_excel("C:\\Users\\0487\\Desktop\\random_data2.xlsx")

# Разделяем данные на признаки и целевую переменную
Z = df[['Sales']]
Y = df['Price']


# Вызов функции для построения графика полиномиальной регрессии

PlotPolyReg(Z, Y, 0)

PlotPolyReg(Z, Y, 1)

PlotPolyReg(Z, Y, 2)

PlotPolyReg(Z, Y, 3)

PlotPolyReg(Z, Y, 4)

PlotPolyReg(Z, Y, 5)

