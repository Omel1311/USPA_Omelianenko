# Импортируем необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Исторические данные о ценах и продажах
prices = np.array([5, 10, 15, 20, 25])  # Цены, при которых продавался товар
sales = np.array([200, 150, 150, 80, 50])  # Соответствующие продажи при этих ценах


# Функция для расчета прибыли
# Прибыль = Цена * Количество продаж
# Мы предполагаем, что количество продаж зависит от цены и хотим найти оптимальную цену для максимизации прибыли
def profit(price, a, b):
    return price * (a - b * price)


# Функция потерь (отрицательная прибыль)
# Используется для минимизации с помощью градиентного спуска
def loss(price, a, b):
    return -profit(price, a, b)


# Функция для расчета градиента функции потерь
# Градиент показывает, как изменяется функция потерь в зависимости от изменения цены
def gradient(price, a, b):
    return - (a - 2 * b * price)


# Параметры для модели, полученные на основе исторических данных
a = 200  # Примерная максимальная начальная точка продаж (объем продаж при очень низкой цене)
b = 5  # Примерный коэффициент чувствительности продаж к цене

# Настройки для градиентного спуска
learning_rate = 0.01  # Скорость обучения (шаг, с которым мы корректируем цену)
num_iterations = 1000  # Количество итераций для градиентного спуска

# Начальная цена, с которой начинаем процесс оптимизации
current_price = 5.0

# Градиентный спуск для поиска оптимальной цены
for i in range(num_iterations):
    # Вычисляем градиент функции потерь при текущей цене
    grad = gradient(current_price, a, b)

    # Корректируем цену в направлении уменьшения функции потерь
    current_price -= learning_rate * grad

    # Обновляем скорость обучения, чтобы уменьшить шаг при приближении к оптимальной точке
    if learning_rate > 0.001:
        learning_rate *= 0.999

# Определяем оптимальную цену, которая максимизирует прибыль
optimal_price = current_price
print(f"Оптимальная цена для максимизации прибыли: ${optimal_price:.2f}")

# Создаем таблицу данных с историческими ценами и объемами продаж
data = {'Цена (USD)': prices, 'Продажи (единицы)': sales}
df = pd.DataFrame(data)

# Выводим таблицу на экран
print(df)

# Построение графика зависимости прибыли от цены
# Создаем диапазон цен от 0 до 30 для анализа изменения прибыли
prices_range = np.linspace(0, 30, 100)

# Вычисляем прибыль для каждой цены в диапазоне
profits = [profit(price, a, b) for price in prices_range]

# Строим график прибыли
plt.plot(prices_range, profits)
plt.xlabel('Цена (USD)')  # Подпись оси X
plt.ylabel('Прибыль')  # Подпись оси Y
plt.title('Зависимость прибыли от цены')  # Заголовок графика

# Добавляем вертикальную линию, показывающую оптимальную цену, найденную методом градиентного спуска
plt.axvline(optimal_price, color='red', linestyle='--', label=f'Оптимальная цена = ${optimal_price:.2f}')

# Добавляем легенду к графику
plt.legend()

# Отображаем график
plt.show()
