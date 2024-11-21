import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from matplotlib.ticker import FuncFormatter # форматирование графика мииллионы, тТЫСЯЧИ И ТД.

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)


# df = pd.read_csv("C://Users//0487//Downloads//fly//Clean_Dataset.csv")
df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")
# df.to_excel('2supermarket_sales.xlsx')

print(df.head())
print(df.shape)
print("*"*100)


# POLINOM 1
def PlotPolly(model, x, y, Name):
    x_new = np.linspace(x.min(), x.max(), 100)  # Используем минимальное и максимальное значение x для более равномерного распределения точек
    y_new = model(x_new)

    plt.plot(x, y, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for duration - Price')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('price')

    plt.show()
    plt.close()

x = df['area']
y = df['price']

# Here we use a polynomial of the 3rd order (cubic)
f = np.polyfit(x, y, 3)
p = np.poly1d(f)

PlotPolly(p, x, y, 'area')

# POLINOM 2
def PlotPolly(model, x, y, Name):
    x_new = np.linspace(x.min(), x.max(), 100)  # Используем минимальное и максимальное значение x для более равномерного распределения точек
    y_new = model(x_new)

    plt.scatter(x, y, marker='.', color='blue', alpha=0.5)  # Полупрозрачные точки в синем цвете
    plt.scatter(x.iloc[1], y.iloc[1], marker='+', color='red')  # Красный домик второй по индексу
    plt.plot(x_new, y_new, '-', color='green')  # Зеленая линия полинома
    plt.title('Polynomial Fit with Matplotlib for duration - Price')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('price')

    plt.show()
    plt.close()

x = df['area']
y = df['price']

# Here we use a polynomial of the 3rd order (cubic)
f = np.polyfit(x, y, 3)
p = np.poly1d(f)

PlotPolly(p, x, y, 'area')

# POLINOM 3

def price_formatter(x, pos):
    return f'{x / 1e6:.0f}M'  # Отображение в миллионах с одним десятичным знаком


def PlotPolly(model, x, y, Name):
    x_new = np.linspace(x.min(), x.max(),
                        100)  # Используем минимальное и максимальное значение x для более равномерного распределения точек
                # return f'{x/1000:,.0f}K - В ТІСЯЧАХ

    y_new = model(x_new)

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='H', color='blue', alpha=0.5)  # Полупрозрачные точки в синем цвете
    ax.scatter(x.iloc[1], y.iloc[1], marker='H', color='red')  # Красный домик второй по индексу
    ax.plot(x_new, y_new, '-', color='red')  # Зеленая линия полинома
    ax.set_title('Polynomial Fit with Matplotlib for duration - Price')
    ax.set_facecolor((0.898, 0.898, 0.898))
    ax.set_xlabel(Name)
    ax.set_ylabel('price')


    formatter = FuncFormatter(price_formatter)
    ax.yaxis.set_major_formatter(formatter)

    plt.show()
    plt.close()


x = df['area']
y = df['price']

# Here we use a polynomial of the 3rd order (cubic)
f = np.polyfit(x, y, 3)
p = np.poly1d(f)

PlotPolly(p, x, y, 'area')


# ax=sns.countplot(x="bedrooms", data=df, hue="basement", color='r')
#
# Добавление значений к каждому столбику
# for p in ax.patches:
#     ax.annotate(format(p.get_height(), '.0f'),
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha = 'center', va = 'center',
#                 xytext = (0, 9),
#                 textcoords = 'offset points')
plt.show()