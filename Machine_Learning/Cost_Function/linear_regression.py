import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# Load the data from an Excel file
data = pd.read_excel("C://Users//0487//Desktop//sales2.xlsx")

# Convert the loaded data to a DataFrame
df = pd.DataFrame(data)

# Split the data into features (Sales) and target variable (Price)
X = df[['Sales']]
y = df['Price']

# Split the data into training and testing sets
# 80% of data will be used for training, and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the linear regression model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Flatten the test data for visualization purposes
X_test_flat = X_test.values.flatten()
mse = mean_squared_error(y_test, y_pred)

# Output the actual and predicted values of the target variable, along with the actual features (Sales)
results = pd.DataFrame({'Actual_price': y_test, 'Predicted_price': y_pred, 'Actual_sales': X_test_flat})
print(results.head())  # Display the first few rows of the results
print(f'MSE: ', {mse})  # Print the Mean Squared Error of the predictions

# Visualize the actual vs predicted values on a scatter plot
plt.scatter(X_test, y_test, color='blue', label='Actual values')  # Actual values as blue dots
plt.plot(X_test, y_pred, color='red', label='Prediction')  # Predicted values as a red line
plt.xlabel('Sales')  # Label for x-axis (Feature)
plt.ylabel('Price')  # Label for y-axis (Target)
plt.legend()
plt.show()
