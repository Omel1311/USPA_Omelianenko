import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")
print(df.head())


Z = df[['area', 'bedrooms', 'bathrooms']]
Y = df['price']


# Multiple LinearRegression
lm = LinearRegression()
lm.fit(Z, Y)

Y_hat = lm.predict(Z)
print(Y_hat[0:5])

fig, ax1 = plt.subplots(figsize=(10, 6))
sns.kdeplot(x=Y, color="r", label="Actual Value", ax=ax1)
sns.kdeplot(Y_hat, color="b", label="Fitted Values", ax=ax1)

plt.title('Actual vs Fitted Values')
plt.xlabel('Price (in dollars)')
plt.ylabel('Z')
plt.legend(title='Legend',
           title_fontsize='large',
           loc='best',# loc='best' is an optional parameter that can be passed to the plt.legend()
           # function in Matplotlib. It specifies the location of the legend on the plot.
           # The loc parameter can take several values, including 'best', 'upper right',
           # 'upper left', 'lower left', 'lower right', 'center left', 'center right', 'lower center', and 'upper center'.
           labels=['Actual Value', 'Fitted Values'])
plt.show()
plt.close()


# PIPLINE Multiple LinearRegression pipeline
pipeline = Pipeline([
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
plt.ylabel('Z')
plt.legend(title='Legend', title_fontsize='large', loc='best', labels=['Actual Value', 'Fitted Values'])
plt.show()

# Оценим точность модели

# Mean Squared Error
mse = mean_squared_error(Y, y_pred)
print(f'Mean Squared Error: {mse:.2f}')


# R^2
r2 = (r2_score(Y, y_pred))
print(f'R^2: {r2:.2f}')


# 2 графика
# Распределение реальных цен
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(Y, kde=True, color='blue', label='Actual Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Actual Prices')
plt.legend()

# Распределение предсказанных цен
plt.subplot(1, 2, 2)
sns.histplot(y_pred, kde=True, color='green', label='Predicted Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of Predicted Prices')
plt.legend()

plt.tight_layout()
plt.show()