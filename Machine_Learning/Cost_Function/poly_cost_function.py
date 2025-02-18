import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Настройки стиля seaborn
sns.set(style="whitegrid")

# Загружаем данные из Excel
df = pd.read_excel("C:\\Users\\0487\\Desktop\\random_data2.xlsx")

# Фильтруем данные, чтобы использовать только положительные значения Sales и Price
df = df[(df['Sales'] > 0) & (df['Price'] > 0)]

# Разделяем данные на признаки и целевую переменную
Z = df[['Sales']].values  # Признак (независимая переменная), преобразуем в массив NumPy
Y = df['Price'].values    # Целевая переменная (зависимая переменная), также в массив NumPy

# Функция для построения графика полиномиальной регрессии и изменения функции стоимости
def plot_poly_regression(Z, Y, max_polynom):
    # Разделение данных на тренировочные и тестовые наборы
    X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

    costs = []  # Список для хранения значений функции стоимости для каждой степени полинома

    # Перебираем степени полинома от 1 до max_polynom
    for polynom in range(1, max_polynom + 1):
        # Преобразование входных признаков в полиномиальные признаки
        pr = PolynomialFeatures(degree=polynom)
        lm = LinearRegression()

        Z_pr = pr.fit_transform(X_train)  # Преобразование входных признаков в полиномиальные признаки
        lm.fit(Z_pr, y_train)  # Обучение модели линейной регрессии на данных с полиномиальными признаками

        # Предсказание на тестовом наборе данных
        y_pred_test = lm.predict(pr.transform(X_test))

        # Расчет функции стоимости (MSE)
        m = len(y_test)
        cost = (1 / (2 * m)) * np.sum((y_pred_test - y_test) ** 2)
        costs.append(cost)

        # Вывод метрик модели для текущей степени полинома
        mse = mean_squared_error(y_test, y_pred_test)
        r2 = r2_score(y_test, y_pred_test)
        print(f'Полином степени {polynom} - Среднеквадратическая ошибка (MSE): {mse:.2f}')
        print(f'Полином степени {polynom} - Коэффициент детерминации (R²): {r2:.3f}')
        print(f'Полином степени {polynom} - Значение функции стоимости: {cost:.2f}')
        print()

    # Построение графика полиномиальной регрессии
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # График 1: Полиномиальная регрессия (для последней степени)
    pr = PolynomialFeatures(degree=max_polynom)
    lm = LinearRegression()
    Z_pr = pr.fit_transform(X_train)
    lm.fit(Z_pr, y_train)

    x_new = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
    x_new_poly = pr.transform(x_new)
    y_new_poly = lm.predict(x_new_poly)

    axes[0].plot(X_test, y_test, 'o', color='blue', alpha=0.5, label='Тестовые данные')
    axes[0].plot(x_new, y_new_poly, '-', color='green', label=f'Полиномиальная регрессия (степень={max_polynom})')
    axes[0].set_title('Полиномиальная регрессия для продаж и цены')
    axes[0].set_facecolor((0.898, 0.898, 0.898))
    axes[0].set_xlabel('Продажи')
    axes[0].set_ylabel('Цена')
    axes[0].set_ylim(0, None)  # Ограничиваем ось Y, чтобы не было отрицательных значений для цены
    axes[0].legend()

    # График 2: Значение функции стоимости для каждой степени полинома
    sns.lineplot(x=range(1, max_polynom + 1), y=costs, marker='o', ax=axes[1], color='b')
    axes[1].set_title('Значение функции стоимости для полиномиальной регрессии')
    axes[1].set_xlabel('Степень полинома')
    axes[1].set_ylabel('Стоимость (MSE)')
    axes[1].set_xticks(range(1, max_polynom + 1))

    # Добавляем сетку для удобства визуального анализа
    axes[0].grid(True)
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

# Пример вызова функции для полиномов от 1 до 5 степени
plot_poly_regression(Z, Y, max_polynom=3)



