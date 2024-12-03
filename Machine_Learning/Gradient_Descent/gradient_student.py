import numpy as np
import matplotlib.pyplot as plt

# Бизнес задача: Оптимизация цены продукта для максимизации прибыли
# Представим, что у нас есть функция прибыли в зависимости от цены продукта: y = -(x - 5)^2 + 25
# Задача - найти оптимальную цену продукта с помощью градиентного спуска

# Инициализация параметров градиентного спуска
learning_rate = 0.1
n_iterations = 1000
x = 10  # начальная точка, произвольное значение

# Производная функции прибыли
def gradient(x):
    return -2 * (x - 5)

# Функция прибыли
def profit_function(x):
    return -(x - 5) ** 2 + 25

# Хранение значений для визуализации
x_values = [x]
y_values = [profit_function(x)]

# Интервалы для визуализации функции
x_axis = np.linspace(0, 10, 100)
y_axis = profit_function(x_axis)

# Градиентный спуск с интерактивной визуализацией
plt.figure(figsize=(10, 6))
for i in range(n_iterations):
    grad = gradient(x)
    x = x + learning_rate * grad
    current_profit = profit_function(x)
    x_values.append(x)
    y_values.append(current_profit)

    # Визуализация текущей точки
    plt.plot(x_axis, y_axis, label='Функция прибыли y = -(x - 5)^2 + 25')
    plt.scatter(x, current_profit, c='r')
    plt.xlabel('Цена продукта')
    plt.ylabel('Прибыль')
    plt.title('Процесс оптимизации цены продукта методом градиентного спуска')
    plt.legend()
    plt.grid()
    plt.pause(0.01)
    plt.clf()

plt.show()

