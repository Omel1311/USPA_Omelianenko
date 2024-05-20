import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")
print(df.head())

Z = df[['area', 'bedrooms',  'bathrooms',  'stories']]
y = df['price']

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]

pipe=Pipeline(Input)

Z = Z.astype(float)
pipe.fit(Z,y)

ypipe=pipe.predict(Z)
print(ypipe[0:4])
print(y[0:4])

# Импортируем необходимые библиотеки
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загрузим данные
iris = load_iris()
print(iris.DESCR)
X = iris.data
y = iris.target

# Разделим данные на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print(X_train[0:5])
# Создадим Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),        # Шаг масштабирования данных
    ('classifier', LogisticRegression()) # Шаг классификации
])

# Обучим модель
pipeline.fit(X_train, y_train)

# Сделаем предсказания
y_pred = pipeline.predict(X_test)

# Оценим точность модели
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')


# Импортируем необходимые библиотеки
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Загрузим данные
california = fetch_california_housing()
X = california.data
y = california.target

# Разделим данные на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создадим Pipeline
pipeline = Pipeline([
    ('scale', StandardScaler()),                # Шаг масштабирования данных
    ('polynomial', PolynomialFeatures(include_bias=False)),  # Шаг полиномиальных признаков
    ('model', LinearRegression())               # Шаг модели линейной регрессии
])

# Обучим модель
pipeline.fit(X_train, y_train)

# Сделаем предсказания
y_pred = pipeline.predict(X_test)

# Оценим модель
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
