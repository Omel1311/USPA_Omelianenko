import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, Ridge


# Функция для построения графика полиномиальной регрессии
def Plot_Poly_Regression(Z,Y,polynom):
    # Разделение данных на тренировочные и тестовые наборы
    X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

    pr = PolynomialFeatures(degree=polynom)  # Создание объекта для генерации полиномиальных признаков
    lm = LinearRegression()  # Создание объекта для модели линейной регрессии

    Z_pr = pr.fit_transform(X_train)  # Преобразование входных признаков в полиномиальные признаки
    lm.fit(Z_pr, y_train)  # Обучение модели линейной регрессии на данных с полиномиальными признаками
    mse = mean_squared_error(y_test, lm.predict(pr.transform(X_test)))
    print(f'Mean Squared Error: {mse:.2f}')
    r2 = r2_score(y_test, lm.predict(pr.transform(X_test)))
    print(f'R² Score: {r2:.3f}')

    fig, ax = plt.subplots()
    # Создание новых точек для построения графика
    x_new = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)

    # Преобразование новых данных для полиномиальной регрессии
    x_new_poly = pr.transform(x_new)
    y_new_poly = lm.predict(x_new_poly)

    # Построение графика на переданной оси `ax`
    ax.plot(X_test, y_test, 'o', color='blue', alpha=0.5, label='Test Data')  # Точки тестовых данных
    ax.plot(x_new, y_new_poly, '-', color='green',
            label=f'Polynomial Regression (degree={polynom})')  # Зеленая линия полинома
    ax.set_title('Polynomial Regression Comparison for Sales - Price')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel('Sales')
    ax.set_ylabel('Price')
    ax.legend()
    plt.tight_layout()
    plt.show()



# Функция для построения графика полиномиальной регрессии с L2 регуляризацией  Ridge
def Plot_Poly_Ridge(Z, Y, polynom):
    # Разделяем данные на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

    # Создаем полиномиальные признаки
    pr = PolynomialFeatures(degree=polynom)
    X_train_poly = pr.fit_transform(X_train)
    X_test_poly = pr.transform(X_test)

    # Создаем модель Ridge (линейная регрессия с L2 регуляризацией)
    ridge = Ridge()

    # Определяем сетку гиперпараметров для подбора
    param_grid = {
        'alpha': [0.01, 0.1, 1, 10, 100]  # коэффициент регуляризации
    }

    # Создаем объект GridSearchCV
    grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')

    # Обучаем GridSearchCV для поиска наилучших гиперпараметров
    grid_search.fit(X_train_poly, y_train)

    # Выводим наилучшие гиперпараметры
    print(f'Лучшие гиперпараметры: {grid_search.best_params_}')
    print(f'Лучший MSE: {grid_search.best_score_}')

    # Используем наилучшую модель для предсказания на тестовой выборке
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test_poly)

    # Оцениваем точность модели Ridge
    mse_ridge = mean_squared_error(y_test, y_pred)
    r2_ridge = r2_score(y_test, y_pred)
    print(f'Среднеквадратическая ошибка (MSE) для Ridge: {mse_ridge:.2f}')
    print(f'Коэффициент детерминации (R²) для Ridge: {r2_ridge:.3f}')

    # Построение графика
    fig, ax = plt.subplots()

    # Создание новых точек для построения графика
    x_new = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
    x_new_poly = pr.transform(x_new)
    y_new_poly = best_model.predict(x_new_poly)

    # Построение графика
    ax.plot(X_test, y_test, 'o', color='blue', alpha=0.5, label='Тестовые данные')  # Точки тестовых данных
    ax.plot(x_new, y_new_poly, '-', color='green',
            label=f'Полиномиальная Ridge регрессия (степень={polynom})')  # Зеленая линия полинома
    ax.set_title('Сравнение полиномиальной Ridge регрессии')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel('Переменная X (например, продажи)')
    ax.set_ylabel('Переменная Y (например, цена)')
    ax.legend()
    plt.tight_layout()
    plt.show()
