from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




def Plot_Linear_Regression(Z, Y):
    # Разделение данных на тренировочные и тестовые наборы
    X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)

    # Обучение модели линейной регрессии
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    # Предсказание на тестовых данных
    y_pred = lm.predict(X_test)

    # Вычисление метрик качества
    mse = mean_squared_error(y_test, y_pred)
    print(f'Среднеквадратическая ошибка (MSE): {mse:.2f}')
    r2 = r2_score(y_test, y_pred)
    print(f'Коэффициент детерминации (R²): {r2:.3f}')

    # Вызов функции compute_cost для расчета стоимости (ошибки)
    w = lm.coef_[0]
    b = lm.intercept_
    cost = compute_cost(X_test.to_numpy().flatten(), y_test.to_numpy(), w, b)
    print(f'Функция стоимости (Cost): {cost:.2f}')

    # Построение графика
    fig, ax = plt.subplots()
    ax.plot(X_test, y_test, 'o', color='blue', alpha=0.5, label='Тестовые данные')
    ax.plot(X_test, y_pred, '-', color='red', label='Линейная регрессия')
    ax.set_title('Линейная регрессия для продаж и цены')
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

# Вызов функции для построения графика линейной регрессии
Plot_Linear_Regression(Z, Y)

