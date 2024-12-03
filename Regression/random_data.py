import numpy as np
import pandas as pd
import random
import datetime
import matplotlib.pyplot as plt

# Setting a seed for reproducibility
np.random.seed(42)

# Generate random dates within the last 1000 days
start_date = datetime.datetime.now() - datetime.timedelta(days=1000)
date_range = [start_date + datetime.timedelta(days=random.randint(0, 1000)) for _ in range(1000)]

# Generate Prices around the optimal price 60
prices = np.random.normal(loc=60, scale=15, size=1000)
prices = np.clip(prices, 10, 120)  # Ensure the price stays within a reasonable range (e.g. 10 to 120)

# Generate Sales with a strong negative correlation to Price
sales = 500 * np.exp(-0.05 * prices) + np.random.normal(scale=10, size=1000)
sales = np.maximum(sales, 0)  # Ensure sales are not negative

# Create the DataFrame
df = pd.DataFrame({'Date': date_range, 'Price': prices, 'Sales': sales.astype(int)})

# Save to Excel
df.to_excel('C:\\Users\\0487\\Desktop\\random_data.xlsx', index=False)

# Plotting the scatter plot to visualize the relationship between Price and Sales
plt.figure(figsize=(10, 6))
plt.scatter(df['Price'], df['Sales'], alpha=0.5, color='b')
plt.title('Sales vs Price')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


df.to_excel('C:\\Users\\0487\\Desktop\\random_data2.xlsx', index=False)
