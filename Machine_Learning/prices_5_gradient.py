import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Загрузка данных
data = pd.read_excel('sales2.xlsx')
prices = np.array(data['Price'])
sales = np.array(data['Sales'])

# Полиномиальная регрессия для прогнозирования продаж
poly = PolynomialFeatures(degree=3)
prices_poly = poly.fit_transform(prices.reshape(-1, 1))
model = LinearRegression()
model.fit(prices_poly, sales)

# Диапазон цен для прогноза (от 20 до 200)
future_prices = np.linspace(20, 200, 200).reshape(-1, 1)
future_prices_poly = poly.transform(future_prices)
predicted_sales = model.predict(future_prices_poly)

# Вычисление прибыли для каждой цены
predicted_profits = future_prices.flatten() * predicted_sales

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(future_prices, predicted_profits, label='Прогноз прибыли', color='green', linewidth=2)
plt.title('Прогноз изменения прибыли при изменении цены', fontsize=14)
plt.xlabel('Цена (USD)', fontsize=12)
plt.ylabel('Прибыль (USD)', fontsize=12)
plt.axvline(future_prices[np.argmax(predicted_profits)], color='red', linestyle='--',
            label=f'Оптимальная цена = ${future_prices[np.argmax(predicted_profits)][0]:.2f}')
plt.legend()
plt.grid()
plt.show()

# Вывод результатов
optimal_price = future_prices[np.argmax(predicted_profits)][0]
optimal_profit = np.max(predicted_profits)
print(f"Оптимальная цена для максимизации прибыли: ${optimal_price:.2f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")
