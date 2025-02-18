import numpy as np
from sklearn.linear_model import LinearRegression

# Матрица признаков (X): площадь (m²) и количество комнат
X = np.array([
    [40, 1],
    [60, 2],
    [80, 3],
    [100, 4],
    [120, 5]
])

# Целевая переменная (цена в тыс. у.е.)
y = np.array([130, 180, 230, 280, 330])  # Реальные цены

# Создаем модель линейной регрессии
model = LinearRegression()

# Обучаем модель на данных
model.fit(X, y)

# Выводим коэффициенты
print("Коэффициенты (веса):", model.coef_)
print("Свободный член (b):", model.intercept_)
