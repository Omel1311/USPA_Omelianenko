# Импорт необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Загрузка данных из Excel-файла
import pandas as pd
file_path = 'C:\\Users\\0487\\Desktop\\sales2.xlsx'

xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Sheet1')

# Извлечение данных о цене и продажах для анализа
X = df['Price'].values.reshape(-1, 1)  # Признак (Цена)
y = df['Sales'].values  # Целевая переменная (Продажи)

# Создание модели полиномиальной регрессии с степенью 3
polynomial_features = PolynomialFeatures(degree=3)
polynomial_model = make_pipeline(polynomial_features, LinearRegression())

# Обучение модели на данных
polynomial_model.fit(X, y)

# Определение функции прибыли на основе данных о продажах и цене
def profit_function(p):
    # Использование модели полиномиальной регрессии для прогнозирования продаж при заданной цене
    sales_prediction = polynomial_model.predict([[p]])[0]
    cost = 20  # Предполагаемая фиксированная себестоимость товара
    return (p - cost) * sales_prediction

# Определение производной функции прибыли с использованием численного метода
def profit_derivative(p, epsilon=1e-5):
    return (profit_function(p + epsilon) - profit_function(p - epsilon)) / (2 * epsilon)

# Установка начальных параметров для градиентного спуска
p_current = 30  # Начальное предположение для цены
alpha = 0.01  # Скорость обучения
tolerance = 0.001  # Порог сходимости
max_iterations = 1000  # Максимальное количество итераций

# Выполнение градиентного спуска для поиска оптимальной цены
for iteration in range(max_iterations):
    gradient = profit_derivative(p_current)
    p_next = p_current - alpha * gradient  # Правило обновления для градиентного спуска

    # Обеспечение того, что цена остаётся положительной
    if p_next < 0:
        p_next = 0

    # Проверка, если изменение меньше установленного порога
    if abs(p_next - p_current) < tolerance:
        break

    p_current = p_next
    print(f"Итерация {iteration + 1}: Цена = {p_current:.2f}, Прибыль = {profit_function(p_current):.2f}")

# Отображение результата
print(f"Оптимальная цена: {p_current:.2f}")
print(f"Максимальная прибыль: {profit_function(p_current):.2f}")

# Построение графика функции прибыли для визуализации оптимизации
prices = np.linspace(0, 50, 500)
profits = [profit_function(p) for p in prices]
plt.plot(prices, profits, label='Функция прибыли')
plt.scatter(p_current, profit_function(p_current), color='red', zorder=5, label='Оптимальная цена')
plt.xlabel('Цена')
plt.ylabel('Прибыль')
plt.title('Функция прибыли и оптимальная цена')
plt.legend()
plt.grid(True)
plt.show()
