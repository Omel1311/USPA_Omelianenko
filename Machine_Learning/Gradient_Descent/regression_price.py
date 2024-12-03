import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Генерация случайных данных для цены и количества продаж
np.random.seed(0)
price = np.random.randint(100, 200, 1000)  # Цена товара
sales = np.where(price > 190, np.random.randint(0, 10, 1000),
                 np.where(price > 150, np.random.randint(0, 30, 1000),
                          np.where(price > 130, np.random.randint(0, 80, 1000),
                                   np.where(price > 110, np.random.randint(0, 95, 1000),
                                            np.random.randint(0, 100, 1000)))))


# Преобразование данных для scikit-learn
X = price.reshape(-1, 1)  # Преобразуем в двумерный массив, так как scikit-learn ожидает двумерный массив для признаков
y = sales

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X, y)

# Прогнозирование количества продаж для заданных цен
new_prices = np.array([120, 140, 160, 180, 200]).reshape(-1, 1)
predicted_sales = model.predict(new_prices)


# Вывод результатов
# for price, sales in zip(new_prices.flatten(), predicted_sales):
for price, sales in zip(new_prices, predicted_sales):
    print(f"Price: {price}, Predicted Sales: {sales}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5)
plt.plot(X, model.predict(X), color='red', label='Linear Regression')
plt.title('Dependence of sales on price')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Находим оптимальную цену
optimal_price = new_prices[np.argmax(predicted_sales)]

# Отображаем вертикальную линию на графике
plt.axvline(x=optimal_price, color='green', linestyle='--', label='Optimal Price')

# Выводим результаты
print(f"Optimal Price: {optimal_price}")

# Обновляем отображение графика
plt.legend()
plt.show()