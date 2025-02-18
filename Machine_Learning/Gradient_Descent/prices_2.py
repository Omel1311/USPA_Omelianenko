import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Исторические данные
prices = np.array([5, 10, 15, 20, 25])
sales = np.array([200,190 , 185, 100, 90])

# Функция прибыли
# Прибыль = Цена * Продажи
# Мы предполагаем, что количество продаж зависит от цены, и хотим найти оптимальную цену

def profit(price, sales):
    return price * sales

# Определение оптимальной цены для максимизации прибыли
profits = [profit(prices[i], sales[i]) for i in range(len(prices))]
print(profits)
optimal_index = np.argmax(profits)
optimal_price = prices[optimal_index]
optimal_profit = profits[optimal_index]

print(f"Оптимальная цена для максимизации прибыли: ${optimal_price:.2f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")

# Построение графиков прибыли и продаж
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# График прибыли в зависимости от цены
ax1.plot(prices, profits, marker='o')
ax1.set_xlabel('Цена (USD)')
ax1.set_ylabel('Прибыль')
ax1.set_title('Зависимость прибыли от цены')
ax1.axvline(optimal_price, color='red', linestyle='--', label=f'Оптимальная цена = ${optimal_price:.2f}')
ax1.legend()

# График продаж (столбчатая диаграмма)
for i in range(len(prices)):
    ax2.bar(prices[i], profits[i], color='skyblue')
    ax2.text(prices[i], profits[i] + 5, f'{sales[i]}', ha='center')
ax2.set_xlabel('Цена (USD)')
ax2.set_ylabel('Продажи (единицы)')
ax2.set_title('Продажи в зависимости от цены')

plt.tight_layout()
plt.show()

# Вывод таблицы на экран
data = {'Цена (USD)': prices, 'Продажи (единицы)': sales, 'Прибыль (USD)': profits}
df = pd.DataFrame(data)
print(df)
