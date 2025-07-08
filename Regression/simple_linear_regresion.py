# Импортируем необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt


# Функция для вычисления среднеквадратичной ошибки (MSE)
def compute_cost(X, y, theta):
    m = len(y)  # Количество примеров в выборке
    predictions = X.dot(theta)  # Предсказания модели
    errors = predictions - y  # Ошибка между предсказанием и реальным значением
    cost = (1 / (2 * m)) * np.sum(errors ** 2)  # Вычисление MSE
    return cost


# Функция градиентного спуска
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)  # Количество примеров
    cost_history = []  # Список для сохранения значений ошибки

    for i in range(iterations):
        gradient = (1 / m) * X.T.dot(X.dot(theta) - y)  # Вычисление градиента
        theta = theta - alpha * gradient  # Обновление параметров
        cost = compute_cost(X, y, theta)  # Вычисление текущего значения ошибки
        cost_history.append(cost)  # Сохранение ошибки

        if i % 10 == 0:  # Вывод информации каждые 10 итераций
            print(f"Итерация {i}: Ошибка = {cost}")

    return theta, cost_history


# Генерация простых данных для примера
np.random.seed(42)  # Фиксируем случайность для воспроизводимости
m = 100  # Количество наблюдений
X = 2 * np.random.rand(m, 1)  # Генерация случайных данных
y = 4 + 3 * X + np.random.randn(m, 1)  # Линейная зависимость с шумом

# Добавляем столбец единиц для учета коэффициента смещения (theta_0)
X_b = np.c_[np.ones((m, 1)), X]  # Добавляем 1 в первый столбец

# Инициализация параметров (весов) модели
initial_theta = np.random.randn(2, 1)  # Случайные начальные коэффициенты
alpha = 0.1  # Коэффициент обучения
iterations = 100  # Количество итераций

# Запуск градиентного спуска
optimal_theta, cost_history = gradient_descent(X_b, y, initial_theta, alpha, iterations)

# Вывод результатов
print("Оптимальные параметры theta:", optimal_theta)

# Визуализация процесса снижения ошибки
plt.plot(range(iterations), cost_history, label='Функция ошибки (MSE)')
plt.xlabel('Итерации')
plt.ylabel('Ошибка')
plt.title('Снижение ошибки в градиентном спуске')
plt.legend()
plt.show()
