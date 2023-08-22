import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Create sample data
data = {'Temperature': [10, 15, 20, 25, 30, 35, 40],
        'DiseaseRate': [5, 10, 30, 70, 100, 120, 130]}

df = pd.DataFrame(data)

# Visualize the data
plt.scatter(df['Temperature'], df['DiseaseRate'], color='blue')
plt.xlabel('Temperature')
plt.ylabel('Disease Rate')
plt.title('Temperature vs. Disease Rate')
plt.show()

# Using Linear Regression
X = df[['Temperature']]
y = df['DiseaseRate']

linear_model = LinearRegression()
linear_model.fit(X, y)
linear_y_pred = linear_model.predict(X)

linear_r2 = r2_score(y, linear_y_pred)

print(f"Linear R-squared score: {linear_r2}")

# Using Polynomial Regression
degree = 2  # Degree of the polynomial
poly = PolynomialFeatures(degree)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
poly_y_pred = poly_model.predict(X_poly)

poly_r2 = r2_score(y, poly_y_pred)

print(f"Polynomial R-squared score: {poly_r2}")
