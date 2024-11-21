import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Исторические данные
prices = np.array([5, 10, 15, 20, 25])
sales = np.array([200, 150, 100, 80, 50])


# Функция прибыли
# Прибыль = Цена * Продажи
# Мы предполагаем, что количество продаж зависит от цены, и хотим найти оптимальную цену

def profit(price, a, b):
    return price * (a - b * price)


# Функция потерь (отрицательная прибыль)
def loss(price, a, b):
    return -profit(price, a, b)


# Градиент функции потерь
def gradient(price, a, b):
    return - (a - 2 * b * price)


# Параметры для модели (полученные из исторических данных)
a = 200  # Примерная начальная точка продаж
b = 5  # Примерный коэффициент чувствительности продаж к цене

# Градиентный спуск для оптимизации цены
learning_rate = 0.01
num_iterations = 1000

# Начальная цена
current_price = 5.0

# Градиентный спуск
for i in range(num_iterations):
    grad = gradient(current_price, a, b)
    current_price -= learning_rate * grad

    # Обновляем learning_rate при необходимости
    if learning_rate > 0.001:
        learning_rate *= 0.999

# Оптимальная цена
optimal_price = current_price
print(f"Оптимальная цена для максимизации прибыли: ${optimal_price:.2f}")

# Вывод таблицы на экран
data = {'Цена (USD)': prices, 'Продажи (единицы)': sales}
df = pd.DataFrame(data)
print(df)

# Построение графика прибыли в зависимости от цены
prices_range = np.linspace(0, 30, 100)
profits = [profit(price, a, b) for price in prices_range]
plt.plot(prices_range, profits)
plt.xlabel('Цена (USD)')
plt.ylabel('Прибыль')
plt.title('Зависимость прибыли от цены')
plt.axvline(optimal_price, color='red', linestyle='--', label=f'Оптимальная цена = ${optimal_price:.2f}')
plt.legend()
plt.show()


