import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных данных о цене и продажах товаров
np.random.seed(4)
num_samples = 200
price = np.random.uniform(50, 100, num_samples)
sales = np.random.normal(loc=100, scale=5, size=num_samples) * (1 - 1 / (price / 100 + 1))

# Округление цены и продаж до целых чисел
price = np.round(price).astype(int)
sales = np.round(sales).astype(int)

# Создание DataFrame с данными
data = pd.DataFrame({'price': price, 'sales': sales})
print(data.head(10))

# Инициализация начальной цены
initial_price = np.max(price)

# Функция стоимости
def cost_function(price, sales):
    predictions = price
    return np.mean((predictions - sales) ** 2)

# Градиент функции стоимости
def compute_gradient(price, sales):
    predictions = price
    error = predictions - sales
    gradient = 2 * np.mean(error)
    return gradient

# Градиентный спуск
def gradient_descent(price, sales, alpha, num_iterations):
    for _ in range(num_iterations):
        gradient = compute_gradient(price, sales)
        price = price - alpha * gradient
    return price

# Подготовка данных
X = data['price']
y = data['sales']

# Выполнение градиентного спуска
optimal_price = gradient_descent(initial_price, y, 0.01, 1000)
print(f"Optimal Price: {optimal_price}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(data['price'], data['sales'], color='blue', label='Исходные данные', alpha=0.5)
plt.plot([initial_price, initial_price], [0, np.max(data['sales'])], color='red', linestyle='--', label='Начальная цена')
plt.plot([optimal_price, optimal_price], [0, np.max(data['sales'])], color='green', label='Оптимальная цена')
plt.xlabel('Цена')
plt.ylabel('Продажи')
plt.legend()
plt.title('Определение оптимальной цены с помощью градиентного спуска')
plt.show()