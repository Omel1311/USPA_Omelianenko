import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)


URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'

airline_data = pd.read_csv(URL)

print(airline_data.head(5))
print(airline_data.columns.to_list())

# data = airline_data.sample(n=500, random_state=42)
data = airline_data.sample(n=500, random_state=42)

# 1. Scatter Plot:

age_array=np.random.randint(25,55,60)
# # Define an array containing salesamount values
#
# income_array=np.random.randint(300000,700000,3000000)
fig=go.Figure()
x = data['Distance']
y = data['DepTime']


# In go.Scatter we define the x-axis data,y-axis data and define the mode as markers with color of the marker as blue
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='blue')))
#
# ## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DeptTime')
# # Display the figure
fig.write_html("plot_interactive.html")

# #2. Line Plot:

line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()
print(line_data.head())

x = line_data['Month']
y = line_data['ArrDelay']
fig=go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Months', yaxis_title='ArrDelay')
fig.write_html("line_plot_interactive.html")

# # 3.Bar Plot:

bar_data = data.groupby('DestState')['Flights'].sum().reset_index()
bar_data = bar_data.sort_values(by='Flights', ascending=False)
print(bar_data.head(40))

x= bar_data['DestState']
y = bar_data['Flights']

fig = px.bar( x=x, y=y, title='Total number of flights to the destination state split by reporting air')
# fig.write_html("bar_interactive.html")
# # fig.show()


# 4.Histogram:

# data['ArrDelay'] = data['ArrDelay'].fillna(0)
# x=data['ArrDelay']
# fig = px.histogram(x=x,title="Total number of flights to the destination state split by reporting air")
# fig.write_html("histogram_interactive.html")

# fig.show()

# 5. Bubble Plot:

##Example 4: Let us illustrate crime statistics of US cities with a bubble chart
#
# bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
# print(bub_data.head())
#
# x  = bub_data['Reporting_Airline']
# y =  bub_data['Flights']
#
# fig = px.scatter(bub_data, x=x, y=y, size=y,
#              hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
# fig.write_html("buble_interactive.html")


# # 6.Pie Plot:

name  = data['DistanceGroup']
val =  data['Flights']
fig = px.pie(values=val, names=name, title='flight propotion by Distance Group')
fig.write_html("pie_interactive.html")

# # 7.Sunburst Charts:

fig = px.sunburst(
     data,
     path=['Month', 'DestStateName'],
     values='Flights',
     title="Flight Distribution Hierarchy"
 )
fig.write_html("sunburst_interactive.html")

