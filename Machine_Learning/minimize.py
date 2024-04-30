from scipy.optimize import minimize
import numpy as np

# Определение границ для переменной
bounds = np.array([[-10.0, 10.0]])
print(bounds)

# Пример использования этих границ, например, в сценарии оптимизации
def objective(x):
    return x**2


result = minimize(objective, x0=1.0, bounds=bounds)
print("Оптимизированное значение x:", result.x)
print("Минимальное значение функции цели:", result.fun)
