import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns



pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)



url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'

df=pd.read_csv(url, header=0)

print(df.head())
lm = LinearRegression()

X = df[['engine-size']]
Y = df['price']

lm.fit(X,Y)

Yhat=lm.predict(X)

print(lm.coef_)
print(lm.intercept_)

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])
print(lm.coef_)
print(lm.intercept_)


lm2 = LinearRegression()
lm2.fit(df[['normalized-losses' , 'highway-mpg']],df['price'])
print(lm2.coef_)
print(lm2.intercept_)

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.show()

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.show()


print('corr', df[["peak-rpm","highway-mpg","price"]].corr())

sns.set (rc = {'figure.figsize':(8, 8)})
dataplot = sns.heatmap(df[["peak-rpm","highway-mpg","price"]].corr(), cmap="YlGnBu", annot=True)
plt.show()
# X=df[['sales']]
# y= df['advertising costs']
#
# model.fit(X,y)
#
# new_x = pd.DataFrame({'sales': [10]})
#
# Y_predict = model.predict(new_x)
#
# r2 = model.score(X,y)
#
#
# print('Y_predict: ', Y_predict)
# print('r2: ', r2)
#
# coof, P_value = stats.pearsonr(df['advertising costs'], df['sales'])
# P_value1 = np.format_float_positional(P_value, trim='-')
# print('coof = ', coof, 'P_value = ', P_value1 )
#




