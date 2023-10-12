import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

np.random.seed(1)
x=np.arange(30)
y = np.random.randint(20,390,size=30)
print(x)
print(y)

fig = go.Figure(data=go.Scatter(x=x, y=y))

fig = px.line(x=x, y=y)


fig.write_html("plot_interactive.html")
fig.show()


#
# plt.plot(x, y, 'o-')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('График y относительно x')
# plt.show()
