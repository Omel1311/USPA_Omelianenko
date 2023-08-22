import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Create sample data
data = {'Time': [1, 2, 3, 4, 5, 6, 7],
        'Sales': [10, 20, 45, 30, 35, 40, 45]}

df = pd.DataFrame(data)

# Visualize the data
plt.scatter(df['Time'], df['Sales'], color='blue')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.title('Time vs. Sales')
plt.show()

# Using Linear Regression
X_linear = df[['Time']]
y_linear = df['Sales']

linear_model = LinearRegression()
linear_model.fit(X_linear, y_linear)
linear_y_pred = linear_model.predict(X_linear)

linear_r2 = r2_score(y_linear, linear_y_pred)

print(f"Linear R-squared score: {linear_r2}")

# Using Polynomial Regression
degree = 2  # Degree of the polynomial
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X_linear)

poly_model = LinearRegression()
poly_model.fit(X_poly, y_linear)
poly_y_pred = poly_model.predict(X_poly)

poly_r2 = r2_score(y_linear, poly_y_pred)

print(f"Polynomial R-squared score: {poly_r2}")
