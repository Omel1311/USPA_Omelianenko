import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Пример создания DataFrame с данными
data = pd.DataFrame({
    'Month': ['January', 'February', 'March'],
    'DestStateName': ['California', 'Texas', 'New York'],
    'Flights': [100, 200, 150]
})

app = dash.Dash(__name__)

# Создание layout для дашборда
app.layout = html.Div([
    html.H1("Flight Distribution Dashboard"),

    dcc.Graph(id='sunburst-chart'),
])


@app.callback(
    Output('sunburst-chart', 'figure'),
    Input('sunburst-chart', 'hoverData')
)
def update_sunburst_chart(hoverData):
    # Создание солнечной диаграммы
    fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights', title='Flight Distribution Hierarchy')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
