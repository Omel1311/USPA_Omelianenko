import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Исторические данные
prices = np.array([5, 10, 15, 20, 25])
sales = np.array([200, 190, 185, 100, 190])

# Предположим линейную зависимость продаж от цены: Sales = a - b * Price
# Начальные параметры
np.random.seed(42)  # Для воспроизводимости
a = 200  # начальное значение a
b = 5    # начальное значение b

# Скорость обучения (learning rate) и количество итераций
learning_rate = 0.0001
iterations = 1000

# Функция прибыли: Profit = Price * Sales
# Sales = a - b * Price, подставляем:
# Profit = Price * (a - b * Price)
def profit(price, a, b):
    return price * (a - b * price)

# Градиенты функции прибыли по a и b
def gradients(prices, sales, a, b):
    grad_a = -2 * np.sum((sales - (a - b * prices)))
    grad_b = -2 * np.sum((sales - (a - b * prices)) * prices)
    return grad_a, grad_b

# Градиентный спуск
def gradient_descent(prices, sales, a, b, learning_rate, iterations):
    history = []  # Для хранения значений прибыли на каждой итерации
    for i in range(iterations):
        grad_a, grad_b = gradients(prices, sales, a, b)
        a -= learning_rate * grad_a
        b -= learning_rate * grad_b

        # Вычисляем общую прибыль на текущей итерации
        total_profit = np.sum(profit(prices, a, b))
        history.append(total_profit)

        # Печать прогресса каждые 100 итераций
        if i % 100 == 0:
            print(f"Итерация {i}: a = {a:.2f}, b = {b:.2f}, Прибыль = {total_profit:.2f}")

    return a, b, history

# Запуск градиентного спуска
a_opt, b_opt, profit_history = gradient_descent(prices, sales, a, b, learning_rate, iterations)

# Оптимальные параметры
print(f"\nОптимальные параметры: a = {a_opt:.2f}, b = {b_opt:.2f}")

# Оптимальная прибыль
optimal_prices = prices
optimal_sales = a_opt - b_opt * optimal_prices
optimal_profits = profit(optimal_prices, a_opt, b_opt)
optimal_price_index = np.argmax(optimal_profits)
optimal_price = optimal_prices[optimal_price_index]
optimal_profit = optimal_profits[optimal_price_index]

print(f"Оптимальная цена для максимизации прибыли: ${optimal_price:.2f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")

# Построение графиков
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# График прибыли в зависимости от цены
ax1.plot(prices, optimal_profits, marker='o', label='Прибыль')
ax1.set_xlabel('Цена (USD)')
ax1.set_ylabel('Прибыль')
ax1.set_title('Зависимость прибыли от цены')
ax1.axvline(optimal_price, color='red', linestyle='--', label=f'Оптимальная цена = ${optimal_price:.2f}')
ax1.legend()

# История прибыли
if profit_history:
    ax2.plot(range(iterations), profit_history, label='История прибыли')
    ax2.set_xlabel('Итерация')
    ax2.set_ylabel('Общая прибыль')
    ax2.set_title('Изменение прибыли в процессе обучения')
    ax2.legend()
else:
    ax2.text(0.5, 0.5, 'Нет данных для отображения', horizontalalignment='center', verticalalignment='center')
    ax2.set_title('История прибыли отсутствует')

plt.tight_layout()
plt.show()

# Вывод итоговой таблицы
result_data = {
    'Цена (USD)': optimal_prices,
    'Продажи (единицы)': optimal_sales.astype(int),
    'Прибыль (USD)': optimal_profits.astype(int)
}
df = pd.DataFrame(result_data)
print(df)
