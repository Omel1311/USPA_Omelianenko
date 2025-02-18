import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Настройки стиля seaborn
sns.set(style="whitegrid")

# Загружаем данные из Excel
df = pd.read_excel("C:\\Users\\0487\\Desktop\\random_data2.xlsx")

# Фильтруем данные, чтобы использовать только положительные значения Sales и Price
df = df[(df['Sales'] > 0) & (df['Price'] > 0)]

# Разделяем данные на признаки и целевую переменную
Z = df[['Sales']].values  # Признак (независимая переменная), преобразуем в массив NumPy
Y = df['Price'].values    # Целевая переменная (зависимая переменная), также в массив NumPy

# Создаем объект линейной регрессии из scikit-learn
model = LinearRegression()

# Обучаем модель на данных (Sales -> Price)
model.fit(Z, Y)

# Получаем значения коэффициента w (наклон линии) и b (смещение)
w = model.coef_[0]  # Коэффициент перед независимой переменной (наклон)
b = model.intercept_  # Свободный член (пересечение с осью Y)

# Выводим значения параметров w и b
print(f"Оптимальное значение w: {w}")
print(f"Оптимальное значение b: {b}")

# Предсказываем значения целевой переменной на основе обученной модели
Y_pred = model.predict(Z)

# Определение функции стоимости
def compute_cost(y_true, y_pred):
    """
    Вычисляет функцию стоимости (Mean Squared Error) для линейной регрессии.

    Args:
      y_true (ndarray (m,)): Фактические значения (целевые значения)
      y_pred (ndarray (m,)): Предсказанные значения

    Returns:
        cost (float): Значение функции стоимости
    """
    # Количество примеров
    m = len(y_true)
    # Среднеквадратичная ошибка (MSE)
    cost = (1 / (2 * m)) * np.sum((y_pred - y_true) ** 2)
    return cost

# Вычисляем значение функции стоимости
cost = compute_cost(Y, Y_pred)
print(f"Значение функции стоимости (MSE): {cost}")

# Альтернативный способ вычисления функции стоимости с использованием sklearn
mse = mean_squared_error(Y, Y_pred)
print(f"Значение функции стоимости (MSE) с использованием sklearn: {mse / 2}")

# Построение двух графиков рядом друг с другом с использованием seaborn
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# График 1: Линия регрессии
sns.scatterplot(x=Z.flatten(), y=Y, color='blue', ax=axes[0], label='Данные')  # Отображение исходных данных
sns.lineplot(x=Z.flatten(), y=Y_pred, color='red', ax=axes[0], label='Линия регрессии')  # Линия регрессии
axes[0].set_xlabel('Продажи (Sales)')
axes[0].set_ylabel('Цена (Price)')
axes[0].set_title('Линейная регрессия: Продажи vs Цена')
axes[0].set_ylim(0, None)  # Устанавливаем минимальное значение оси Y равным 0, чтобы не отображать отрицательные значения
axes[0].legend()

# График 2: Функция стоимости
w_values = np.linspace(-2, 4, 100)  # Генерируем 100 значений w от -2 до 4
cost_values = [compute_cost(Y, w * Z.flatten() + b) for w in w_values]  # Вычисляем функцию стоимости для каждого w

sns.lineplot(x=w_values, y=cost_values, color='b', ax=axes[1])
axes[1].set_xlabel('Значение w')
axes[1].set_ylabel('Значение функции стоимости (Cost)')
axes[1].set_title('График функции стоимости в зависимости от параметра w')

# Добавляем сетку для удобства визуального анализа
axes[0].grid(True)
axes[1].grid(True)

# Отображаем оба графика
plt.tight_layout()
plt.show()

