from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sb


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'

df = pd.read_csv(url)
df.replace('?', np.NAN, inplace=True)
print(df.head())

lm=LinearRegression()
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X,Y)
print(lm.intercept_)

Yhat = lm.coef_
print(Yhat)
