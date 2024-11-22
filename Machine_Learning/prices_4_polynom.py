import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.polynomial import Polynomial

# Исторические данные
data = pd.read_excel('C:\\Users\\0487\\Desktop\\sales.xlsx')

# Удаление NaN значений, если они есть
data.dropna(inplace=True)

# Преобразование данных в массивы numpy
prices = np.array(data['Price'])
sales = np.array(data['Sales'])
print(data.head())

# Функция прибыли
# Прибыль = Цена * Продажи
# Мы предполагаем, что количество продаж зависит от цены, и хотим найти оптимальную цену
def profit(price, sales):
    return price * sales

# Определение оптимальной цены для максимизации прибыли
profits = [profit(prices[i], sales[i]) for i in range(len(prices))]

# Преобразование в массив numpy для работы с индексами
profits = np.array(profits)

# Проверка, нет ли NaN или бесконечных значений в прибыли
valid_indices = np.isfinite(profits)
prices = prices[valid_indices]
sales = sales[valid_indices]
profits = profits[valid_indices]

# Полиномиальная регрессия для графика прибыли
polynomial_degree = 8  # степень полинома
coefs = np.polyfit(prices, profits, polynomial_degree)
polynomial = np.poly1d(coefs)

# Генерация точек для линии регрессии
prices_fit = np.linspace(prices.min(), prices.max(), 100)
profits_fit = polynomial(prices_fit)

# Определение оптимальной цены для максимизации прибыли
optimal_index = np.argmax(profits)
optimal_price = prices[optimal_index]
optimal_profit = profits[optimal_index]

print(f"Оптимальная цена для максимизации прибыли: ${optimal_price:.2f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")

# Построение графиков прибыли и продаж
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# График прибыли в зависимости от цены с полиномиальной регрессией
ax1.scatter(prices, profits, color='blue', label='Фактические данные')
ax1.plot(prices_fit, profits_fit, color='green', linestyle='-', label='Полиномиальная регрессия')
ax1.set_xlabel('Цена (USD)')
ax1.set_ylabel('Прибыль')
ax1.set_title('Зависимость прибыли от цены')
ax1.axvline(optimal_price, color='red', linestyle='--', label=f'Оптимальная цена = ${optimal_price:.2f}')
ax1.legend()

# График продаж (столбчатая диаграмма)
for i in range(len(prices)):
    ax2.bar(prices[i], sales[i], color='skyblue')
    ax2.text(prices[i], sales[i] + 5, f'{sales[i]}', ha='center')
ax2.set_xlabel('Цена (USD)')
ax2.set_ylabel('Продажи (единицы)')
ax2.set_title('Продажи в зависимости от цены')

plt.tight_layout()
plt.show()

# Вывод таблицы на экран
data = {'Цена (USD)': prices, 'Продажи (единицы)': sales, 'Прибыль (USD)': profits}
df = pd.DataFrame(data)
print(df)