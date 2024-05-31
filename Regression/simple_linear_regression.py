import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df = pd.read_csv("C://Users//0487//Downloads//Housing.csv")
print(df.shape)
print("*"*100)
print(df.head(10))


# LinearRegression
fig, axs = plt.subplots(1, 2, figsize=(15, 6))
lm = LinearRegression()

X = df[['area']]
y = df['price']
lm.fit(X, y)
Yhat1 = lm.predict(X)
print(Yhat1[0:5])
sns.regplot(x=X, y=y, data=df, scatter_kws={'color':'seagreen'}, line_kws={'color':'peru'}, ax=axs[0])
axs[0].set_title('Linear Regression for Олія')



# Создание pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Масштабирование признаков
    ('regressor', LinearRegression())  # Линейная регрессия
])

# Обучение модели на всех данных
pipeline.fit(X, y)

# Прогнозирование на тех же данных
y_pred = pipeline.predict(X)
print(y_pred[0:5])

# Визуализация результатов с помощью Seaborn

sns.scatterplot(x=y, y=y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted Prices')
plt.show()

print('The R-square is: ', lm.score(X, y))


