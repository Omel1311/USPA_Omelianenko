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
import seaborn as sb
import plotly.express as px
import mplcursors
#_______________________________________________________________

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

#_______________________________________________________________

file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df = pd.read_csv(file_name)
print(df.shape)
print(df.head(10))

#_______________________________________________________________

data_types = df.dtypes
print(data_types)
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
colors_list = ['c', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
unique_floor = df['floors'].value_counts().to_frame()
unique_floor.plot(kind = 'pie',
                  y='floors',
                  labels=None,
                  pctdistance=1.2,
                  startangle=10,
autopct='%1.1f%%'
                  )
plt.title('Floors', y=1.1, fontsize = 15)
plt.axis('equal')
print(unique_floor)
#_______________________________________________________________
lm = LinearRegression()
width = 10
height = 8
plt.figure(figsize=(width, height))
sns.regplot(x="floors", y="price", data=df, scatter_kws={'color':'seagreen'}, line_kws={'color':'peru'})
plt.title('floors/price')
plt.ylim(0,)

#
#_______________________________________________________________
width = 10
height = 8
plt.figure(figsize=(width, height))
sns.boxplot(y='price', x='floors', data=df)
plt.title('Boxplot of Price by Floors')
plt.xlabel('Floors')
plt.ylabel('Price')
plt.show()
#_______________________________________________________________

width = 10
height = 8
plt.figure(figsize=(width, height))
sns.boxplot(y='price', x='condition', data=df)
plt.title('Boxplot of Price by Condition')
plt.xlabel('Condition/Price')
plt.ylabel('Price')

#_______________________________________________________________
# # count, bin_edges = np.histogram(df["condition"])
# plt.figure(figsize=(width, height))
# df["condition"].plot(kind='hist', figsize=(8, 5), color='teal',  xticks=bin_edges)
# plt.title('Histogram of Price by Condition')
# # add a title to the histogram

#_______________________________________________________________

width = 15
height = 10

# Створення підграфіків (5 графіків)
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(width, height))

# Розбивка даних на 5 груп
conditions = df['condition'].unique()

# Побудова графіків для кожної умови
for i, condition in enumerate(conditions):
    ax = axes[i]
    ax.hist(df[df['condition'] == condition]['price'], bins=5, color='teal')  # Розбивка на 5 бінів
    ax.set_title(f'Histogram of Price for Condition {condition}')
    ax.set_xlabel('Price')
    ax.set_ylabel('Count')

# Відображення графіків
plt.tight_layout()
plt.show()

#_______________________________________________________________
lm = LinearRegression()
width = 10
height = 8
plt.figure(figsize=(width, height))
sns.regplot(x="condition", y="price", data=df, scatter_kws={'color':'seagreen'}, line_kws={'color':'peru'})
plt.ylim(0,)
plt.title('Scatter of Price by Condition')
plt.show()
#_______________________________________________________________________________________________
print('!'*200)
print(df.corr()['price'].sort_values())
#______________________________________________________________________________________________________________________________

X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
print('R^2 для лонг', lm.score(X, Y))
#_______________________________________________________________
print('*'*20)

X = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
Yhat=lm.predict(X)
print('The output of the first four predicted value is (sqft_living): ', Yhat[0:4])
print('R^2 (sqft_living): ', lm.score(X, Y))
#___________________________________________________________________________________________________________________
print('*'*20)
lm1 = LinearRegression()
X = df[["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]]
Y = df['price']
lm1.fit(X,Y)
Yhat=lm1.predict(X)
print('The output of the first four predicted value is (11 VAR): ', Yhat[0:4])
print('R^2 (11 VAR): ', lm1.score(X, Y))
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
print('Pipeline model (pipline)', predictions[0:4])
r_squared = pipe.score(X, y)
print('Pipeline r^2= ', r_squared)

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
plt.figure(figsize=(20, 10))
cmap='viridis'
# "viridis", coolwarm', 'plasma', 'inferno', 'magma', 'YlGnBu'
dataplot = sb.heatmap(df.corr(),cmap=cmap, annot=True)
# dataplot = sb.heatmap(df.corr(),cmap="YlGnBu", annot=True)
dataplot.set_title('heatmap')
plt.show()
#_______________________________________________________________

# lm = LinearRegression()
# width = 10
# height = 8
# plt.figure(figsize=(width, height))
# ax = sns.regplot(x="yr_built", y="price", data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
# # Function to display information on hover
#
# plt.ylim(0,)
# plt.show()
# #_______________________________________________________________
#
# # Create a scatter plot using Plotly
# fig = px.scatter(df, x="yr_built", y="price", text=df['price'])
#
# # Update the layout to display the hover information
# fig.update_traces(textposition='top center')
#
# # Show the plot
# fig.show()
#______________________________________________________________________________________________________________________________
width = 10
height = 8
plt.figure(figsize=(width, height))

# Create a regression plot with a blue scatter plot and a red regression line
ax = sns.regplot(x="yr_built", y="price", data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'})

# Define the hover function
def hover(sel):
    ind = sel.target[0].index
    condition_value = df.iloc[ind]['condition']
    sel.annotation.set_text(f'Condition: {condition_value}')

# Connect the hover event to the hover function
cursor = mplcursors.cursor(hover=True)

plt.ylim(0,)
plt.show()









