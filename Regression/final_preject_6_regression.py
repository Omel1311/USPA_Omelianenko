import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from  sklearn.model_selection import train_test_split
import matplotlib
from sklearn.linear_model import Ridge

#_______________________________________________________________

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

#_______________________________________________________________

file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df = pd.read_csv(file_name)
print(df.head(50))

#_______________________________________________________________

data_types = df.dtypes
print(data_types)
print(df.describe())
#_______________________________________________________________

df.drop(columns=["id", "Unnamed: 0"], axis=1, inplace=True)
print(df.describe())
#_______________________________________________________________

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)
mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())
#_______________________________________________________________

unique_floor = df['floors'].value_counts().to_frame()
print(unique_floor)
#_______________________________________________________________

sns.boxplot(y='price', x='waterfront', data=df)
plt.title('Boxplot of Price by Waterfront View')
plt.xlabel('Waterfront View')
plt.ylabel('Price')
plt.show()
#_______________________________________________________________

lm = LinearRegression()
width = 10
height = 8
plt.figure(figsize=(width, height))
sns.regplot(x="sqft_above", y="price", data=df)
plt.ylim(0,)
plt.show()
#_______________________________________________________________________________________________

print(df.corr()['price'].sort_values())
#_______________________________________________________________

X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
print(lm.score(X, Y))
#_______________________________________________________________
print('*'*20)
Y = df['price']
X = df[['sqft_living']]
lm = LinearRegression()
lm.fit(X,Y)
Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])
print('R^2: ', lm.score(X, Y))
#___________________________________________________________________________________________________________________
print('*'*20)
lm1 = LinearRegression()
X = df[["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]]
Y = df['price']
lm1.fit(X,Y)
Yhat=lm1.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])
print('R^2: ', lm1.score(X, Y))
#_______________________________________________________________
print('*'*20)

features = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement", "view",
            "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]
X = df[features]
y = df['price']

Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(X, y)
predictions = pipe.predict(X)
print(predictions)
pipe.fit(X, y)
r_squared = pipe.score(X, y)
print('r^2= ', r_squared)

#_______________________________________________________________
features = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement", "view",
            "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]

# Extract the features and target variable
X = df[features]
y = df['price']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and fit a Ridge regression model
ridge = Ridge(alpha=0.1)  # Regularization parameter is set to 0.1
ridge.fit(X_train_scaled, y_train)

# Make predictions on the test set
predictions = ridge.predict(X_test_scaled)

# Calculate the R-squared for the test set
r_squared = r2_score(y_test, predictions)

print(f'R-squared on test data: {r_squared:.4f}')
#_______________________________________________________________

