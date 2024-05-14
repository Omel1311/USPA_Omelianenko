import matplotlib.pyplot as plt

# Исторические данные о продажах (цена, количество продаж)
sales_data = [(5, 100), (10, 80), (15, 60), (20, 40), (25, 20)]

# Затраты на производство одной единицы товара
initial_cost = 2

# Фиксированные затраты
fixed_costs = 50

# Функция для расчета прибыли
def calculate_profit(price, sales_data, initial_cost, fixed_costs):
    total_sales = sum(sales for _, sales in sales_data if price > 0)
    return (price - initial_cost) * total_sales - fixed_costs

# Функция градиентного спуска
def gradient_descent(sales_data, initial_cost, fixed_costs, initial_price, learning_rate, num_iterations):
    price = initial_price
    for _ in range(num_iterations):
        gradient = sum((price - cost) * sales for cost, sales in sales_data if price > 0)
        price -= learning_rate * gradient
    return price

# Начальная цена и параметры градиентного спуска
initial_price = 15
learning_rate = 0.001
num_iterations = 100

# Нахождение оптимальной цены
optimal_price = gradient_descent(sales_data, initial_cost, fixed_costs, initial_price, learning_rate, num_iterations)
print("Оптимальная цена для максимизации прибыли:", optimal_price)

# Построение графика зависимости прибыли от цены
prices = range(0, 30)
profits = [calculate_profit(price, sales_data, initial_cost, fixed_costs) for price in prices]

plt.plot(prices, profits)
plt.xlabel('Цена')
plt.ylabel('Прибыль')
plt.title('Зависимость прибыли от цены')
plt.axvline(x=optimal_price, color='r', linestyle='--', label='Оптимальная цена')
plt.legend()
plt.show()


