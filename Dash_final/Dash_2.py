import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import folium

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

print(df.describe())
print(df.head())
print(df.columns)

# TASK 1.1: Develop a Line chart using the functionality of pandas to show how automobile sales fluctuate from year to year
#
# plt.figure(figsize=(10, 6))
# df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
# df_line.plot(kind='line')
# plt.xticks(list(range(1980, 2024)), rotation=75)
# plt.xlabel('Year')
# plt.ylabel('Sales Volume')
# plt.title('Automobile Sales during Recession')
# plt.text(1982, 650, '1981-82 Recession')
# plt.text(1991, 650, '1991 Recession')
# plt.text(2001, 740, '2000-2001 Recession')
# plt.text(2009, 1050, '2007-2009 Recession')
# plt.legend(['Automobile Sales over Time'], loc='upper left')
#
#
#
# # TASK 1.2: Plot different lines for categories of vehicle type and analyse the trend to answer the question
# # Is there a noticeable difference in sales trends between different vehicle types during recession periods?¶
# recession_df = df[df['Recession'] == 1]
# plt.figure(figsize=(13, 8))
# df_Mline = recession_df.groupby(['Year', 'Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()
# df_Mline.set_index('Year', inplace=True)
# df_Mline = df_Mline.groupby(['Vehicle_Type'])['Automobile_Sales']
# df_Mline.plot(kind='line')
# plt.xticks(list(range(1980, 2024)), rotation=75)
# plt.xlabel('Year')
# plt.ylabel('Sales Volume')
# plt.title('Sales Trend Vehicle-wise during Recession')
# plt.legend(title='Vehicle Type', loc='upper right')
# df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
# plt.show()
#
#
#
# #TASK 1.3: Use the functionality of Seaborn Library to create a visualization to compare the
# # sales trend per vehicle type for a recession period with a non-recession period.¶
# new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession', data=new_df)
# plt.ylabel('Automobile_Sales')
# plt.xlabel('Period')
# plt.title('Average Automobile Sales during Recession and Non-Recession')
# plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
#
#
#
# recession_data = df[df['Recession'] == 1]
# dd = df.groupby(['Recession', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
#
# # Calculate the total sales volume by vehicle type during recessions
# sales_by_vehicle_type = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
#
# # Create the grouped bar chart using seaborn
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Recession', y='Automobile_Sales', hue='Vehicle_Type', data=dd)
# plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
# plt.xlabel('Period')
# plt.ylabel('Average Sales')
# plt.title('Vehicle-Wise Sales during Recession and Non-Recession Period')
#
# plt.show()
#
# #TASK 1.4: Use sub plotting to compare the variations in GDP during recession
# # and non-recession period by developing line plots for each period.¶
#
# rec_data = df[df['Recession'] == 1]
# non_rec_data = df[df['Recession'] == 0]
#
# # Figure
# fig = plt.figure(figsize=(12, 6))
#
# # Create different axes for subploting
# ax0 = fig.add_subplot(1, 2, 1)  # add subplot 1 (1 row, 2 columns, first plot)
# ax1 = fig.add_subplot(1, 2, 2)  # add subplot 2 (1 row, 2 columns, second plot).
#
# # plt.subplot(1, 2, 1)
# sns.lineplot(x='Year', y='GDP', data=rec_data, label='Recession', ax=ax0)
# ax0.set_xlabel('Year')
# ax0.set_ylabel('GDP')
# ax0.set_title('GDP Variation during Recession Period')
#
# sns.lineplot(x='Year', y='GDP', data=non_rec_data, label='No Recession', ax=ax1)
# ax1.set_xlabel('Year')
# ax1.set_ylabel('GDP')
# ax1.set_title('GDP Variation during No Recession Period')
#
#
# plt.tight_layout()
# plt.show()

# TASK 1.5: Develop a Bubble plot for displaying the impact of seasonality on Automobile Sales.

# non_rec_data = df[df['Recession'] == 0]

# size =df['Seasonality_Weight']  # for bubble effect
#
# sns.scatterplot(data=df, x='Month', y='Automobile_Sales', size=size, hue=size)
#
# # you can further include hue='Seasonality_Weight', legend=False)
#
# plt.xlabel('Month')
# plt.ylabel('Automobile_Sales')
# plt.title('Seasonality impact on Automobile Sales')
# # From this plot, it is evident that seasonality has not affected on the overall sales. However, there is a drastic raise in sales in the month of April
# plt.show()


# TASK 1.6: Use the functionality of Matplotlib to develop a scatter plot to identify the correlation between average vehicle price relate to the sales volume during recessions.¶
# Create dataframes for recession and non-recession period

# rec_data = df[df['Recession'] == 1]
# plt.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'])
#
# plt.xlabel('Consumer_Confidence')
# plt.ylabel('Automobile_Sales')
# plt.title('Consumer Confidence and Automobile Sales during Recessions')
#
# rec_data = df[df['Recession'] == 1]
# plt.scatter(rec_data['Price'], rec_data['Automobile_Sales'])
#
# plt.xlabel('Price')
# plt.ylabel('Automobile_Sales')
# plt.title('Relationship between Average Vehicle Price and Sales during Recessions')
# # There is not much relation!
# plt.show()


# TASK 1.7: Create a pie chart to display the portion of advertising expenditure of XYZAutomotives during recession and non-recession periods.¶
# How did the advertising expenditure of XYZAutomotives change during recession and non-recession periods?

# Filter the data
# Rdata = df[df['Recession'] == 1]
# NRdata = df[df['Recession'] == 0]
#
# # Calculate the total advertising expenditure for both periods
# RAtotal = Rdata['Advertising_Expenditure'].sum()
# NRAtotal = NRdata['Advertising_Expenditure'].sum()
#
# # Create a pie chart for the advertising expenditure
# plt.figure(figsize=(8, 6))
#
# labels = ['Recession', 'Non-Recession']
# sizes = [RAtotal, NRAtotal]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#
# plt.title('Advertising Expenditure during Recession and Non-Recession Periods')
#
# plt.show()


# TASK 1.8: Develop a pie chart to display the total Advertisement expenditure for each vehicle type during recession period.

# Filter the data
# Rdata = df[df['Recession'] == 1]
#
# # Calculate the sales volume by vehicle type during recessions
# VTsales = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
# print(VTsales.head())
#
# # Create a pie chart for the share of each vehicle type in total sales during recessions
# plt.figure(figsize=(8, 6))
#
# labels = VTsales.index
# sizes = VTsales.values
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#
# plt.title('Share of Each Vehicle Type in Total Sales during Recessions')
# # During recession the advertisements were mostly focued on low price range vehicle. A wise decision!
# plt.show()


# TASK 1.9: Develop a countplot to analyse the effect of the unemployment rate on vehicle type and sales during the Recession Period.¶
# data = df[df['Recession'] == 1]
#
# plt.figure(figsize=(10, 6))
#
# sns.countplot(data=data, x='unemployment_rate', hue='Vehicle_Type')
#
# plt.xlabel('Unemployment Rate')
# plt.ylabel('Count')
# plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
# plt.legend(loc='upper right')
# # Hint: You can right lick on the plot and then click on "Save image as" option to save it on your local machine*
# plt.show()



# OPTIONAL : TASK 1.10 Create a map on the hightest sales region/offices of the company during recession period¶

import urllib.request

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/us-states.json'
filename = "us-states.json"

try:
    urllib.request.urlretrieve(url, filename)
    print('Файл успешно скачан и сохранен как', filename)
except urllib.error.URLError as e:
    print('Произошла ошибка при скачивании файла:', e)


# Filter the data for the recession period and specific cities
recession_data = df[df['Recession'] == 1]

# Calculate the total sales by city
sales_by_city = recession_data.groupby('City')['Automobile_Sales'].sum().reset_index()

# Create a base map centered on the United States
map1 = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Create a choropleth layer using Folium
choropleth = folium.Choropleth(
    geo_data= 'us-states.json',  # GeoJSON file with state boundaries
    data=sales_by_city,
    columns=['City', 'Automobile_Sales'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Automobile Sales during Recession'
).add_to(map1)


# Add tooltips to the choropleth layer
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name'], labels=True)
)

# Display the map
map1.save('recession_map.png')