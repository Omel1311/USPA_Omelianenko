import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge

# Создаем пример данных
data = pd.read_excel("C://Users//0487//Desktop//sales2.xlsx")

df = pd.DataFrame(data)


# Разделяем данные на признаки и целевую переменную
X = df[['Sales']]
y = df['Price']

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Создаем модель линейной регрессии
model = LinearRegression()

# Обучаем модель
model.fit(X_train, y_train)

# Делаем прогноз на тестовой выборке
y_pred = model.predict(X_test)

X_test_flat = X_test.values.flatten()
mse = mean_squared_error(y_test, y_pred)


# Выводим результаты прогнозирования
results = pd.DataFrame({'Actual_price': y_test, 'Predicted_price': y_pred, 'Actual_sales': X_test_flat})
print(results.head())
print(f'MSE: ', {mse})

# Визуализация результатов
plt.scatter(X_test, y_test, color='blue', label='Фактические значения')
plt.plot(X_test, y_pred, color='red', label='Прогноз')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show()
