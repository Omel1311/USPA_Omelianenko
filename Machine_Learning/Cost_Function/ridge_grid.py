import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Создаем пример данных
data = pd.read_excel("C:\\Users\\0487\\Desktop\\random_data.xlsx")

df = pd.DataFrame(data)

# Разделяем данные на признаки и целевую переменную
Z = df[['Sales']]
Y = df['Price']

S = df[['Sales']]
P = df['Price']



# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(Z, Y, test_size=0.2, random_state=42)
X_test_flat = X_test.values.flatten()
# Создаем модель Ridge (линейная регрессия с L2 регуляризацией)
ridge = Ridge()
# Определяем сетку гиперпараметров для подбора
param_grid = {
    'alpha': [0.01, 0.1, 1, 10, 100]  # коэффициент регуляризации
}
# Создаем объект GridSearchCV
grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
# Обучаем GridSearchCV для поиска наилучших гиперпараметров
grid_search.fit(X_train, y_train)
# Выводим наилучшие гиперпараметры
print(f'Лучшие гиперпараметры: {grid_search.best_params_}')
print(f'Лучший MSE: {grid_search.best_score_}')
# Используем наилучшую модель для предсказания на тестовой выборке
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Оценим точность модели ridge
mse_ridge = mean_squared_error(y_test, y_pred)
r2_ridge = r2_score(y_test, y_pred)
print(f'Mean Squared Error Ridge: {mse_ridge:.2f}')
print(f'R² Score Ridge: {r2_ridge:.3f}')




# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(S, P, test_size=0.2, random_state=42)

model = LinearRegression()
# Обучаем модель
model.fit(X_train, y_train)

# Делаем прогноз на тестовой выборке
y_pred = model.predict(X_test)

X_test_flat = X_test.values.flatten()

mse_ridge = mean_squared_error(y_test, y_pred)
r2_ridge = r2_score(y_test, y_pred)
print(f'Mean Squared Errore: {mse_ridge:.2f}')
print(f'R² Score: {r2_ridge:.3f}')


# POLYNOMIAL REGRESSION
pr = PolynomialFeatures(degree=3)  # Создание объекта для генерации полиномиальных признаков
lm = LinearRegression()  # Создание объекта для модели линейной регрессии

Z_pr = pr.fit_transform(Z)  # Преобразование входных признаков Z в полиномиальные признаки
lm.fit(Z_pr, Y)  # Обучение модели линейной регрессии на данных с полиномиальными признаками

Y_pred_poly = lm.predict(Z_pr)

# Создание двух подграфиков в одном окне (горизонтально)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

def KDEPlot(x, y, Name, ax):
    # Первый график: KDE для фактических и предсказанных значений
    sns.kdeplot(x=P, color="r", label="Actual Value", ax=ax)
    sns.kdeplot(Y_pred_poly, color="b", label="Fitted Values", ax=ax)
    ax.set_title('Actual vs Fitted Values Polynomial Regression (KDE)')
    ax.set_xlabel('Price (in dollars)')
    ax.set_ylabel('Density')
    ax.legend(title='Legend', title_fontsize='large', loc='best', labels=['Actual Value', 'Fitted Values'])

def KDEPlot_ridge(x, y, Name, ax):
    # Первый график: KDE для фактических и предсказанных значений
    sns.kdeplot(x=Y, color="r", label="Actual Value", ax=ax)
    sns.kdeplot(Y_pred_poly, color="b", label="Fitted Values", ax=ax)
    ax.set_title('Ridge Actual vs Fitted Values Polynomial Regression (KDE)')
    ax.set_xlabel('Price (in dollars)')
    ax.set_ylabel('Density')
    ax.legend(title='Legend', title_fontsize='large', loc='best', labels=['Actual Value', 'Fitted Values'])

# Второй график: Сравнение линейной и полиномиальной регрессии
def PlotReg_ridge(model_poly, poly_transformer, model_lin, x, y, Name, ax):
    # Создание новых точек для построения графика
    x_new = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)

    # Преобразование новых данных для полиномиальной регрессии
    x_new_poly = poly_transformer.transform(x_new)
    y_new_poly = model_poly.predict(x_new_poly)

    # Получение предсказаний для линейной регрессии
    y_new_lin = model_lin.predict(x_new)  # Подаем исходные данные для Ridge, без полиномиальных преобразований

    # Построение графика на переданной оси `ax`
    ax.plot(x, y, 'o', color='blue', alpha=0.5, label='Test Data')  # Точки тестовых данных
    ax.plot(x_new, y_new_poly, '-', color='green', label='Polynomial Regression (degree=3)')  # Зеленая линия полинома
    ax.plot(x_new, y_new_lin, '--', color='red', label='Linear Regression (Ridge)')  # Красная пунктирная линия линейной регрессии
    ax.set_title('Linear and Polynomial Regression Comparison for Sales - Price')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel(Name)
    ax.set_ylabel('Price')
    ax.legend()



# Вызов функции для построения первого графика
KDEPlot(X_test, y_test, 'Sales', ax1)

# Вызов функции для построения третьего графика
KDEPlot_ridge(X_test, y_test, 'Sales', ax2)

# Вызов функции для построения второго графика
PlotReg(lm, pr, best_model, X_test, y_test, 'Sales', ax3)

# Показ графиков
plt.tight_layout()
plt.show()
