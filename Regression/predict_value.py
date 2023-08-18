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


# Regression Plot
width = 12
height = 10
# plt.figure(figsize=(width, height))
# sns.regplot(x="highway-mpg", y="price", data=df)
# plt.ylim(0,)
# plt.show()
#
# plt.figure(figsize=(width, height))
# sns.regplot(x="peak-rpm", y="price", data=df)
# plt.ylim(0,)
# plt.show()



#  Verify correlation
# print('corr', df[["peak-rpm","highway-mpg","price"]].corr())
# sns.set (rc = {'figure.figsize':(8, 8)})
# dataplot = sns.heatmap(df[["peak-rpm","highway-mpg","price"]].corr(), cmap="YlGnBu", annot=True)
# plt.show()



#  Residual Plot
# width = 12
# height = 10
# plt.figure(figsize=(width, height))
# sns.residplot(x=df['highway-mpg'],y=df['price'])
# plt.show()



#   Multiple Linear Regression
Y_hat=lm.predict(Z)
plt.figure(figsize=(width, height))

ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)

plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()



