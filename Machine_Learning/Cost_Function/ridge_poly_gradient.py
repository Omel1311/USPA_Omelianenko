import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

# Создаем пример данных
data = pd.read_excel("C:\\Users\\0487\\Desktop\\random_data.xlsx")

df = pd.DataFrame(data)

# Разделяем данные на признаки и целевую переменную
Z = df[['Sales']]
Y = df['Price']

# Разделение данных на тренировочные и тестовые наборы
X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

# POLYNOMIAL REGRESSION
pr = PolynomialFeatures(degree=3)  # Создание объекта для генерации полиномиальных признаков
lm = LinearRegression()  # Создание объекта для модели линейной регрессии

Z_pr = pr.fit_transform(X_train)  # Преобразование входных признаков в полиномиальные признаки
lm.fit(Z_pr, y_train)  # Обучение модели линейной регрессии на данных с полиномиальными признаками

fig, ax = plt.subplots()

# Функция для построения графика полиномиальной регрессии
def PlotPolyReg(model_poly, poly_transformer, x_train, y_train, x_test, y_test, Name):
    # Создание новых точек для построения графика
    x_new = np.linspace(x_train.min(), x_train.max(), 100).reshape(-1, 1)

    # Преобразование новых данных для полиномиальной регрессии
    x_new_poly = poly_transformer.transform(x_new)
    y_new_poly = model_poly.predict(x_new_poly)

    # Построение графика на переданной оси `ax`
    ax.plot(x_test, y_test, 'o', color='blue', alpha=0.5, label='Test Data')  # Точки тестовых данных
    ax.plot(x_new, y_new_poly, '-', color='green', label='Polynomial Regression (degree=3)')  # Зеленая линия полинома
    ax.set_title('Polynomial Regression Comparison for Sales - Price')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel(Name)
    ax.set_ylabel('Price')
    ax.legend()

# Вызов функции для построения графика полиномиальной регрессии
PlotPolyReg(lm, pr, X_train, y_train, X_test, y_test, 'Sales')

# Показ графиков
plt.tight_layout()
plt.show()
