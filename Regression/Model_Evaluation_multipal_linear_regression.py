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

# print(df.shape)
#
# num_cols_before = df.shape[1]
# empty_cols = df.isnull().all(axis=0)
# df = df.drop(df.columns[empty_cols], axis=1)
# num_cols_after = df.shape[1]
# num_cols_removed = num_cols_before - num_cols_after
# print(f"Количество удаленных столбцов: {num_cols_removed}")
# print( num_cols_after )

# df = df.fillna(0)    # Заполнение пустых значений нулями
#
# df = df.reset_index(drop=True)


# df.to_excel('C://Users//0487//Desktop//ww4.xlsx')


# Multiple LinearRegression
lm = LinearRegression()
# График для столбца 'Олія'
Z = df[['Олія', 'Нафтопродукти', 'Хімічні', 'СУХОВАНТАЖНІ СИПУЧІ']]
Y = df['ВСЬОГО ВАНТАЖІВ']
lm.fit(Z, Y)

Y_hat = lm.predict(Z)
print(Y_hat[0:5])
print(Y[0:5])

ax1 = sns.distplot(x=Y, hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for ВСЬОГО ВАНТАЖІВ')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
plt.legend(title='Legend', title_fontsize='large', loc='best', labels=['Actual Value', 'Fitted Values'])

plt.show()
plt.close()


# как изменится значение 'ВСЬОГО ВАНТАЖІВ' при изменении значения Нафтопродукти

# Создаем копию исходного DataFrame
df_predict = df.copy()

# Заменяем второе значение 'Нафтопродукти' на 900
df_predict.at[1, 'Нафтопродукти'] = 1000
print(df_predict.head())
# Создаем массив Z для прогноза
Z_predict = df_predict[['Олія', 'Нафтопродукти', 'Хімічні', 'СУХОВАНТАЖНІ СИПУЧІ']]

# Прогнозируем значение 'ВСЬОГО ВАНТАЖІВ'
Y_predicted = lm.predict(Z_predict)
print(Y_predicted[1])