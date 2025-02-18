import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score


# Функция для построения графика полиномиальной регрессии
def Plot_Poly_Regression(Z, Y, polynom):
    if polynom == 0:
        print("Степень полинома не может быть 0 для полиномиальной регрессии")
        return

    # Разделение данных на тренировочные и тестовые наборы
    X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

    pr = PolynomialFeatures(degree=polynom)
    lm = LinearRegression()

    Z_pr = pr.fit_transform(X_train)  # Преобразование входных признаков в полиномиальные признаки
    lm.fit(Z_pr, y_train)  # Обучение модели линейной регрессии на данных с полиномиальными признаками
    mse = mean_squared_error(y_test, lm.predict(pr.transform(X_test)))
    print(f'Полином степени {polynom} - Среднеквадратическая ошибка (MSE): {mse:.2f}')
    r2 = r2_score(y_test, lm.predict(pr.transform(X_test)))
    print(f'Полином степени {polynom} - Коэффициент детерминации (R²): {r2:.3f}')

    fig, ax = plt.subplots()
    x_new = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
    x_new_poly = pr.transform(x_new)
    y_new_poly = lm.predict(x_new_poly)

    ax.plot(X_test, y_test, 'o', color='blue', alpha=0.5, label='Тестовые данные')
    ax.plot(x_new, y_new_poly, '-', color='green', label=f'Полиномиальная регрессия (степень={polynom})')
    ax.set_title('Полиномиальная регрессия для продаж и цены')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel('Продажи')
    ax.set_ylabel('Цена')
    ax.legend()
    plt.tight_layout()
    plt.show()


# Функция для построения графика полиномиальной регрессии с L2 регуляризацией Ridge
def Plot_Poly_Ridge(Z, Y, polynom):
    if polynom == 0:
        print("Степень полинома не может быть 0 для полиномиальной регрессии")
        return

    # Разделяем данные на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

    # Создаем полиномиальные признаки
    pr = PolynomialFeatures(degree=polynom)
    X_train_poly = pr.fit_transform(X_train)
    X_test_poly = pr.transform(X_test)

    # Нормализация данных
    scaler = StandardScaler()
    X_train_poly = scaler.fit_transform(X_train_poly)
    X_test_poly = scaler.transform(X_test_poly)

    # Создаем модель Ridge
    ridge = Ridge()

    # Определяем сетку гиперпараметров для подбора
    param_grid = {
        'alpha': [0.01, 0.1, 1, 10, 100]
    }

    # Создаем объект GridSearchCV
    grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')

    # Обучаем GridSearchCV для поиска наилучших гиперпараметров
    grid_search.fit(X_train_poly, y_train)

    # Выводим наилучшие гиперпараметры
    print(f'Полином степени {polynom} - Лучшие гиперпараметры: {grid_search.best_params_}')
    print(f'Полином степени {polynom} - Лучший MSE: {grid_search.best_score_}')

    # Используем наилучшую модель для предсказания на тестовой выборке
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test_poly)

    # Оцениваем точность модели Ridge
    mse_ridge = mean_squared_error(y_test, y_pred)
    r2_ridge = r2_score(y_test, y_pred)
    print(f'Полином степени {polynom} - Среднеквадратическая ошибка (MSE) для Ridge: {mse_ridge:.2f}')
    print(f'Полином степени {polynom} - Коэффициент детерминации (R²) для Ridge: {r2_ridge:.3f}')

    # Построение графика
    fig, ax = plt.subplots()
    x_new = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
    x_new_poly = pr.transform(x_new)
    x_new_poly_scaled = scaler.transform(x_new_poly)
    y_new_poly = best_model.predict(x_new_poly_scaled)

    ax.plot(X_test, y_test, 'o', color='blue', alpha=0.5, label='Тестовые данные')
    ax.plot(x_new, y_new_poly, '-', color='green', label=f'Полиномиальная Ridge регрессия (степень={polynom})')
    ax.set_title('Сравнение полиномиальной Ridge регрессии')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel('Продажи')
    ax.set_ylabel('Цена')
    ax.legend()
    plt.tight_layout()
    plt.show()


# Создаем пример данных
df = pd.read_excel("C:\\Users\\0487\\Desktop\\random_data2.xlsx")

# Разделяем данные на признаки и целевую переменную
Z = df[['Sales']]
Y = df['Price']

# Вызов функции для построения графика полиномиальной регрессии
for i in range(1, 6):
    Plot_Poly_Regression(Z, Y, i)

print('*' * 100)

# Вызов функции для построения графика полиномиальной Ridge регрессии
for i in range(1, 6):
    Plot_Poly_Ridge(Z, Y, i)
