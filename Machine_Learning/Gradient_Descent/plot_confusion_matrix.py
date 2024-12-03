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
for price, sales in zip(new_prices.flatten(), predicted_sales):
    print(f"Price: {price}, Predicted Sales: {sales}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.5)
plt.plot(X, model.predict(X), color='red', label='Linear Regression')
plt.title('Dependence of sales on price')
plt.xlabel('Price')
plt.ylabel('Sales')

# Находим оптимальную цену с использованием градиентного спуска
def cost_function(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = np.sum((predictions - y) ** 2) / (2 * m)
    return cost

def gradient(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    grad = X.T.dot(predictions - y) / m
    return grad

def gradient_descent(X, y, theta, learning_rate, iterations):
    cost_history = np.zeros(iterations)
    for i in range(iterations):
        theta = theta - learning_rate * gradient(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history

X_b = np.c_[np.ones((X.shape[0], 1)), X]
theta = np.zeros(X_b.shape[1])
learning_rate = 0.0001
iterations = 1000

theta_optimal, _ = gradient_descent(X_b, y, theta, learning_rate, iterations)
optimal_price = -theta_optimal[1] / theta_optimal[2]

# Выводим результат
print(f"Optimal Price: {optimal_price}")

# Отображаем оптимальную цену на графике
plt.axvline(x=optimal_price, color='green', linestyle='--', label='Optimal Price')

# Обновляем отображение графика
plt.legend()
plt.show()

