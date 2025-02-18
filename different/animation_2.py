import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import matplotlib.dates as mdates

# Load the data
sales_data = pd.read_excel("C:\\Users\\0487\\Desktop\\sales2.xlsx")

# Convert 'date' column to datetime if not already
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Sort data by date in chronological order
sales_data = sales_data.sort_values(by='date')

# Calculate the mean sales value
mean_sales = sales_data['Sales'].mean()

# Prepare figure and axis
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Sales Over Time')

# Set up the x and y limits
ax.set_xlim(sales_data['date'].min(), sales_data['date'].max())
ax.set_ylim(sales_data['Sales'].min() - 10, sales_data['Sales'].max() + 10)

# Set date format and frequency for x-axis
date_format = mdates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3)) # Show every 3rd date
fig.autofmt_xdate(rotation=45)  # Rotate dates for better readability

# Initialize the line object
line, = ax.plot([], [], color='blue', linewidth=2)
# Initialize scatter plot for points above the mean
scatter = ax.scatter([], [], color='red', label='Above Mean')

# Initialize data for animation
x_data, y_data = [], []
x_above, y_above = [], []

def update(frame):
    # Append the next data point
    x_data.append(sales_data['date'].iloc[frame])
    y_data.append(sales_data['Sales'].iloc[frame])

    # Check if the current point is above the mean
    if sales_data['Sales'].iloc[frame] > mean_sales:
        x_above.append(sales_data['date'].iloc[frame])
        y_above.append(sales_data['Sales'].iloc[frame])

    # Update the line data
    line.set_data(x_data, y_data)

    # Update the scatter plot data
    scatter.set_offsets(list(zip(x_above, y_above)))

    return line, scatter

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=len(sales_data), interval=200, blit=True
)

# Display the plot
plt.legend()
plt.show()
