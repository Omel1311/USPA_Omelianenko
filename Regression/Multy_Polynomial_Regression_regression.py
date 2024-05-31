import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)


# df = pd.read_csv("C://Users//0487//Downloads//fly//Clean_Dataset.csv")
df = pd.read_csv("C://Users//0487//Downloads//CarPrice_Assignment.csv")


print(df.head())
print(df.shape)
print("*"*100)

# MULTI POLINOM

Z = df[['enginesize', 'curbweight', 'citympg', 'highwaympg']]
Y = df['price']

pr = PolynomialFeatures(degree=1)  # Создание объекта для генерации полиномиальных признаков
lm = LinearRegression()  # Создание объекта для модели линейной регрессии

Z_pr = pr.fit_transform(Z)  # Преобразование входных признаков Z в полиномиальные признаки
lm.fit(Z_pr, Y)  # Обучение модели линейной регрессии на данных с полиномиальными признаками

Y_pred = lm.predict(Z_pr)
print(Y_pred[0:5])

# Визуализация результатов с линией идеального предсказания
fig, ax1 = plt.subplots(figsize=(10, 6))

sns.kdeplot(x=Y, color="r", label="Actual Value", ax=ax1)
sns.kdeplot(Y_pred, color="b", label="Fitted Values", ax=ax1)
plt.title('Actual vs Fitted Values Multiple Linear Regression')
plt.xlabel('Price (in dollars)')
plt.ylabel('Density')
plt.legend(title='Legend', title_fontsize='large', loc='best', labels=['Actual Value', 'Fitted Values'])
# Оценим точность модели

# Mean Squared Error
mse = mean_squared_error(Y, Y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# R^2
r2 = (r2_score(Y, Y_pred))
print(f'R^2: {r2:.3f}')



# PIPLINE Multiple LinearRegression
pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=1)),  # Полиномиальные признаки степени 2
    ('scaler', StandardScaler()),  # Масштабирование признаков
    ('regressor', LinearRegression())  # Линейная регрессия
])
# Обучение модели на всех данных
pipeline.fit(Z, Y)

# Прогнозирование на тех же данных
y_pred = pipeline.predict(Z)
print(y_pred[0:5])


# Визуализация распределений реальных и предсказанных цен
fig, ax1 = plt.subplots(figsize=(10, 6))

sns.kdeplot(x=Y, color="r", label="Actual Value", ax=ax1)
sns.kdeplot(y_pred, color="b", label="Fitted Values", ax=ax1)

plt.title('Actual vs Fitted Values using Pipline Multiple Linear Regression')
plt.xlabel('Price (in dollars)')
plt.ylabel('Density')
plt.legend(title='Legend', title_fontsize='large', loc='best', labels=['Actual Value', 'Fitted Values'])
plt.show()

# Оценим точность модели

# Mean Squared Error
mse = mean_squared_error(Y, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# R^2
r2 = (r2_score(Y, y_pred))
print(f'R^2: {r2:.3f}')

