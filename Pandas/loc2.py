import pandas as pd
import plotly.express as px
x = {'Name': ['Rose','John', 'Jane', 'Mary'],
     'ID': [1, 2, 3, 4],
     'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)
w = df.iloc[0,2]


print(w)
# Create a scatter plot using Plotly
fig = px.scatter(df, x="Name", y="Salary", text=df['Department'])

# Update the layout to display the hover information
fig.update_traces(textposition='top center')

# Show the plot
fig.show()