import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Scatter Plot:
#
# age_array=np.random.randint(25,55,60)
# # Define an array containing salesamount values
#
# income_array=np.random.randint(300000,700000,3000000)
# fig=go.Figure()
#
# #Next we will create a scatter plot by using the add_trace function and use the go.scatter() function within it
# # In go.Scatter we define the x-axis data,y-axis data and define the mode as markers with color of the marker as blue
# fig.add_trace(go.Scatter(x=age_array, y=income_array, mode='markers', marker=dict(color='blue')))
#
# ## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
# fig.update_layout(title='Economic Survey', xaxis_title='Age', yaxis_title='Income')
# # Display the figure
# # fig.show()
#
# # 2. Line Plot:
#
# ##Example 2: Let us illustrate the sales of bicycles from Jan to August last year using a line chart
# # Define an array containing numberofbicyclessold
#
# numberofbicyclessold_array=[50,100,40,150,160,70,60,45]
#
# # Define an array containing months
# months_array=["Jan","Feb","Mar","April","May","June","July","August"]
#
# ##First we will create an empty figure using go.Figure()
# fig=go.Figure()
# #Next we will create a line plot by using the add_trace function and use the go.scatter() function within it
# # In go.Scatter we define the x-axis data,y-axis data and define the mode as lines with color of the marker as green
#
# fig.add_trace(go.Scatter(x=months_array, y=numberofbicyclessold_array, mode='lines', marker=dict(color='green')))
# ## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
#
# fig.update_layout(title='Bicycle Sales', xaxis_title='Months', yaxis_title='Number of Bicycles Sold')
# # Display the figure
# # fig.show()
#
#
#
# # 3.Bar Plot: ##Example 3: Let us illustrate the average pass percentage of classes from grade 6 to grade 10
#
# # Define an array containing scores of students
# score_array=[80,90,56,88,95]
# # Define an array containing Grade names
# grade_array=['Grade 6','Grade 7','Grade 8','Grade 9','Grade 10']
#
# fig = px.bar( x=grade_array, y=score_array, title='Pass Percentage of Classes')
# # fig.show()


# 4.Histogram:

# Код, который вы предоставили, генерирует массив из 200 значений,
# распределенных нормально с средним значением 160 и стандартным отклонением 11.
heights_array = np.random.normal(160, 3, 200)

## Use plotly express histogram chart function px.histogram.Provide input data x to the histogram
fig = px.histogram(x=heights_array,title="Distribution of Heights")

# fig.show()

# 5. Bubble Plot:

##Example 4: Let us illustrate crime statistics of US cities with a bubble chart
# Create a dictionary having city,numberofcrimes and year as 3 keys
crime_details = {
    'City': ['Chicago', 'Chicago', 'Austin', 'Austin', 'Seattle', 'Seattle'],
    'Numberofcrimes': [1000, 1200, 400, 700, 350, 1500],
    'Year': ['2007', '2008', '2007', '2008', '2007', '2008'],
}

# create a Dataframe object with the dictionary
df = pd.DataFrame(crime_details)

## Group the number of crimes by city and find the total number of crimes per city
bub_data = df.groupby('City')['Numberofcrimes'].sum().reset_index()

##Display the grouped dataframe
## Bubble chart using px.scatter function with x ,y and size varibles defined.Title defined as Crime Statistics
fig = px.scatter(bub_data, x="City", y="Numberofcrimes", size="Numberofcrimes",
                 hover_name="City", title='Crime Statistics', size_max=60)
fig.write_html("plot_interactive.html")
# fig.show()



# # 6.Pie Plot:
#
# # Random Data
# exp_percent= [20, 50, 10,8,12]
# house_holdcategories = ['Grocery', 'Rent', 'School Fees','Transport','Savings']
# # Use px.pie function to create the chart. Input dataset.
# # Values parameter will set values associated to the sector. 'exp_percent' feature is passed to it.
# # labels for the sector are passed to the `house hold categoris` parameter.
# fig = px.pie(values=exp_percent, names=house_holdcategories, title='Household Expenditure')
#
# fig.write_html("plot_interactive.html")
# # fig.show()

# 7.Sunburst Charts:
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
    title="Family chart"
)
fig.write_html("plot_interactive.html")
fig.show()

