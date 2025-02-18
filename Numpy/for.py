import numpy as np

# Матрица признаков (X): площадь (m²) и количество комнат
X = np.array([
    [40, 1],
    [60, 2],
    [80, 3],
    [100, 4],
    [120, 5]
])

# Увеличиваем каждый элемент X на [100, 2]
for i in range(len(X)):
    X[i] += np.array([100, 2])

# Добавляем новые строки, где каждый элемент умножается на 10 и 2
for s in range(len(X)):
    new_row = np.array([[X[0] * 10, X[1] * 2]])  # Создаём новую строку
    X = np.vstack((X, new_row))  # Добавляем её в X

print(X)
