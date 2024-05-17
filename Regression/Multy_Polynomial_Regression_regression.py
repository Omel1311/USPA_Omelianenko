import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)


# df = pd.read_csv("C://Users//0487//Downloads//fly//Clean_Dataset.csv")
df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")
# df.to_excel('2supermarket_sales.xlsx')

print(df.head())
print(df.shape)
print("*"*100)

# MULTI POLINOM

Z = df[['area']]
Y = df['price']

pr = PolynomialFeatures(degree=1)  # Создание объекта для генерации полиномиальных признаков
lm = LinearRegression()  # Создание объекта для модели линейной регрессии

Z_pr = pr.fit_transform(Z)  # Преобразование входных признаков Z в полиномиальные признаки
lm.fit(Z_pr, Y)  # Обучение модели линейной регрессии на данных с полиномиальными признаками


# Предполагая, что у вас есть данные для предсказания (например, Z_test)
# Сделайте предсказания с использованием модели
Y_pred = lm.predict(Z_pr)
print(Y_pred[0:5])
print(Y[0:5])

# Визуализация результатов с линией идеального предсказания
plt.scatter(Y, Y_pred,alpha=0.5)
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], '--', color='red')  # Линия идеального предсказания
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs. Predicted Prices for Polynomial Multiple Regression with Ideal Prediction Line')
plt.show()
