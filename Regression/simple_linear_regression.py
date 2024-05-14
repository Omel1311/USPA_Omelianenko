import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df = pd.read_excel('C://Users//0487//Desktop//ww2.xlsx')

print(df.shape)

num_cols_before = df.shape[1]
empty_cols = df.isnull().all(axis=0)
df = df.drop(df.columns[empty_cols], axis=1)
num_cols_after = df.shape[1]
num_cols_removed = num_cols_before - num_cols_after
print(f"Количество удаленных столбцов: {num_cols_removed}")
print( num_cols_after )

df = df.fillna(0)    # Заполнение пустых значений нулями

df = df.reset_index(drop=True)
print(df.head(10))

# df.to_excel('C://Users//0487//Desktop//ww4.xlsx')


# LinearRegression
fig, axs = plt.subplots(1, 2, figsize=(15, 6))
lm = LinearRegression()
# График для столбца 'Олія'
X = df[['Хімічні']]
Y = df['ВСЬОГО ВАНТАЖІВ']
lm.fit(X, Y)
Yhat1 = lm.predict(X)
sns.regplot(x=X, y=Y, data=df, scatter_kws={'color':'seagreen'}, line_kws={'color':'peru'}, ax=axs[0])
axs[0].set_title('Linear Regression for Олія')

# We look at the spread of the residuals:
# # - If the points in a residual plot are
# randomly spread out around the x-axis, then a linear model is appropriate for the data

sns.residplot(x=X,y=Y)
axs[1].set_title('Residual Plot')

plt.ylim(0,)
plt.show()

