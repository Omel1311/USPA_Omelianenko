import pandas as pd  # Импорт библиотеки pandas и присвоение ей псевдонима pd
import numpy as np  # Импорт библиотеки numpy и присвоение ей псевдонима np
import matplotlib.pyplot as plt  # Импорт модуля matplotlib.pyplot для построения графиков и присвоение ему псевдонима plt
import seaborn as sns  # Импорт библиотеки seaborn для визуализации данных
from sklearn.linear_model import LinearRegression  # Импорт класса LinearRegression из модуля sklearn.linear_model
from matplotlib.ticker import FuncFormatter  # Импорт класса FuncFormatter для форматирования графика

pd.set_option('display.max_columns', 100)  # Установка максимального количества отображаемых столбцов в pandas
pd.set_option('display.width', 500)  # Установка ширины отображения данных в pandas
pd.set_option('display.max_rows', 500)  # Установка максимального количества отображаемых строк в pandas

df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")  # Чтение данных из файла Housing.csv в DataFrame df
print(df.head())



def price_formatter(x, pos):
    return f'{x/1e6:.1f}M'  # Функция форматирования чисел для отображения в миллионах с одним десятичным знаком

# Функция для построения графика полиномиальной регрессии
def PlotPolly(model, x, y, Name):
    X_mean = np.mean(x)
    Y_mean = np.mean(y)

    x_new = np.linspace(x.min(), x.max(), 100)  # Генерация новых значений x для плавной линии регрессии
    y_new = model(x_new)  # Получение предсказанных значений на основе модели

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # Создание графика с двумя осями

    axs[0].plot(x, y, '.', alpha=0.5)  # Отображение исходных данных точками синего цвета
    axs[0].scatter(X_mean, Y_mean,marker='+', color='red')
    axs[0].plot(x_new, y_new, '-', color='green')  # Отображение полиномиальной регрессии зеленой линией

    axs[0].set_title('Polynomial Fit with Matplotlib for duration - Price')  # Установка заголовка для первого графика
    axs[0].set_facecolor((0.898, 0.898, 0.898))  # Установка цвета фона графика в формате RGBA
    axs[0].set_xlabel(Name)  # Установка подписи оси x
    axs[0].set_ylabel('price')  # Установка подписи оси y

    lm = LinearRegression()  # Создание объекта линейной регрессии
    X = x.values.reshape(-1, 1)  # Преобразование x в двумерный массив для sklearn
    Y = y.values.reshape(-1, 1)  # Преобразование y в двумерный массив для sklearn
    lm.fit(X, Y)  # Обучение модели линейной регрессии
    lm.predict(X)  # Предсказание значений для сравнения

    # Отображение Грфика 2

    sns.regplot(x=x, y=y, data=df, scatter_kws={'color': 'seagreen'}, line_kws={'color': 'peru'}, ax=axs[1])  # Отображение линейной регрессии с помощью seaborn
    axs[1].set_title('Linear Regression for Price ~ Area')  # Установка заголовка для второго граф

    formatter = FuncFormatter(price_formatter)
    axs[0].yaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.show()
    plt.close()



    print(f'X_mean = {X_mean}, Y_mean = {Y_mean}')  # Вывод среднего значения X_mean, Y_mean)

x = df['area']
y = df['price']

# Here we use a polynomial of the 3rd order (cubic)
f = np.polyfit(x, y, 3)
p = np.poly1d(f)

PlotPolly(p, x, y, 'area')


def PlotReg(model_poly, model_lin, x, y, Name):
    X_mean = np.mean(x)
    Y_mean = np.mean(y)
    x_new = np.linspace(x.min(), x.max(), 100)  # Используем минимальное и максимальное значение x для более равномерного распределения точек
    y_new_poly = model_poly(x_new)
    y_new_lin = model_lin.predict(x_new.reshape(-1, 1))
    fig, ax = plt.subplots()
    ax.plot(x, y, '.', alpha=0.5)  # Точки в синем цвете
    ax.scatter(X_mean, Y_mean, marker='+', color='r',
               label=f'Mean: {x.name}, {int(round(X_mean))}, {y.name}, {int(round(Y_mean))}')  # Отображение названий колонок x и y
    ax.plot(x_new, y_new_poly, '-', color='green', label='Polynomial Regression')  # Зеленая линия полинома
    ax.plot(x_new, y_new_lin, '--', color='red', label='Linear Regression')  # Красная пунктирная линия линейной регрессии
    ax.set_title('Linear and Polynomial Regression Comparison for duration - Price')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel(Name)
    ax.set_ylabel('price')

    formatter = FuncFormatter(price_formatter)
    ax.yaxis.set_major_formatter(formatter)

    ax.legend()
    plt.show()
    plt.close()


# Polynomial regression (График 3)
f_poly = np.polyfit(x, y, 4)
p_poly = np.poly1d(f_poly)

# Linear regression
lm = LinearRegression()
X = x.values.reshape(-1, 1)
Y = y.values.reshape(-1, 1)
lm.fit(X, Y)

PlotReg(p_poly, lm, x, y, 'area')

print('corr', df[["area","parking","price","bathrooms", "bedrooms"]].corr())
sns.set (rc = {'figure.figsize':(8, 8)})
dataplot = sns.heatmap(df[["area","parking","price","bathrooms", "bedrooms"]].corr(),  cmap="YlGnBu", annot=True)
plt.show()
