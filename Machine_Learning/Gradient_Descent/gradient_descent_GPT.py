import numpy as np
import matplotlib.pyplot as plt
import random

# Сгенерируем искусственные данные
np.random.seed(0)
# x = 2 * np.random.randn(10, 1)  # 100 точек данных
# y = 77 + 9 * x + np.random.randn(10, 1)  # линейная зависимость с шумом

x = random.randint(1,20)
y = random.randint(1,20)
print("x=",x)
print("y", y)
w = 0  # вес (наклон линии), начальное предположение
b = 0  # смещение (пересечение с осью Y), начальное предположение

# Параметры обучения
learning_rate = 0.01  # маленький шаг для обновления параметров
n_iterations = 50  # количество итераций для обучения

# Градиентный спуск
for i in range(n_iterations):
    y_pred = w * x + b  # текущее предсказание модели

    # Вычисление градиентов
    dw = -2 * np.sum(x * (y - y_pred)) / len(x)  # градиент по w
    db = -2 * np.sum(y - y_pred) / len(y)  # градиент по b

    # Обновление параметров
    w -= learning_rate * dw  # обновляем вес
    b -= learning_rate * db  # обновляем смещение

    # Необязательно: печать процесса обучения каждые 100 итераций
    if i % 100 == 0:
        loss = np.mean((y - y_pred) ** 2)  # среднеквадратичная ошибка
        print(f"Iteration {i}: w = {w}, b = {b}, Loss = {loss}")

# Вывод финальных параметров модели
print(f"Final parameters: w = {w}, b = {b}")

# Построение графика
plt.scatter(x, y, color='blue', label='Data points')  # исходные данные
plt.plot(x, w * x + b, color='red', label='Regression line')  # линия регрессии
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with Gradient Descent')
plt.legend()
plt.show()

import numpy as np

# Одно случайное число из стандартного нормального распределения
single_value = np.random.randn()

# Одномерный массив из 5 случайных чисел
one_dimensional_array = np.random.randn(5)

# Двумерная матрица 2x3 из случайных чисел
two_dimensional_array = np.random.randn(2, 3)

print("Одно случайное число:", single_value)
print("Одномерный массив:", one_dimensional_array)
print("Двумерная матрица:", two_dimensional_array)
