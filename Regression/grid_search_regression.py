import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

# Чтение данных из файла Housing.csv
df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")
print(df.info())

print(df['furnishingstatus'].value_counts())


print(df[df['furnishingstatus'] == 'furnished']['price'].mean())
print(df[(df['furnishingstatus'] == 'furnished') & (df['basement']== 'yes')].head())
print(df[(df['bathrooms'] > 2)]['price'].min())

# Преобразование категориальных признаков в числовые с помощью OneHotEncoding
# df = pd.get_dummies(df, columns=['prefarea', 'furnishingstatus'])
# print(df.head())
# print(df.info())
# Разделение данных на признаки (X) и целевую переменную (y)
X = df.drop('price', axis=1)
y = df['price']
print(X.head())

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#

print()

# # Создание и обучение модели линейной регрессии
# model = LinearRegression()
# model.fit(X_train, y_train)
#
# # Предсказание целевой переменной на тестовой выборке
# y_pred = model.predict(X_test)
#
# # Оценка модели на тестовой выборке
# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error:", mse)
