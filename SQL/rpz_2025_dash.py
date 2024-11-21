import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

# Ініціалізація додатку Dash
app = dash.Dash(__name__)

# Словник зі скороченнями для назв філій
abbreviations = {
    "Білгород-Дністровська ДП \"АМПУ\"": "Білгород-Дністровська",
    "Одеська філія ДП \"АМПУ\"": "ОФ",
    "ПІВДЕННА ФІЛІЯ ДП \"АМПУ\"": "Південна філія",
    "Ренійська філія ДП \"АМПУ\"": "РФ",
    "Миколаївська філія ДП \"АМПУ\"": "МФ",
    "ФІЛІЯ \"ДЕЛЬТА-ЛОЦМАН\" ДЕРЖАВНОГО ПІДПРИЄМСТВА \"АДМІНІСТРАЦІЯ МОРСЬКИХ ПОРТІВ УКРАЇНИ\"": "Дельта-Лоцман",
    "Чорноморська філія ДП \"АМПУ\"": "ЧФ",
    "Ізмаїльська філія ДП \"АМПУ\"": "ІФ",
    "Філія \"Ольвія\" ДП \"АМПУ\"": "Ольвія",
    "ФІЛІЯ \"ДНОПОГЛИБЛЮВАЛЬНИЙ ФЛОТ\" ДЕРЖАВНОГО ПІДПРИЄМСТВА \"АДМІНІСТРАЦІЯ МОРСЬКИХ ПОРТІВ УКРАЇНИ\"": "ДФ",
    "Філія \"Усть-Дунайськ\" ДП \"АМПУ\"": "Усть-Дунайськ",
    "ФІЛІЯ \"ЧОРНОМОРНДІПРОЄКТ\" ДЕРЖАВНОГО ПІДПРИЄМСТВА \"АДМІНІСТРАЦІЯ МОРСЬКИХ ПОРТІВ УКРАЇНИ\"": "ЧорноморНДІпроєкт",
    "ДП \"АМПУ\"": "АМПУ",
    "Філія \"ЧорноморНДІпроєкт\" ДП \"АМПУ\"": "ЧорноморНДІпроєкт",
    "Херсонська філія ДП \"АМПУ\"": "ХФ",
    "nan": "Не визначено"
}


# Функція для завантаження даних з Google Sheets
def load_data():
    sheet_id = '1QD65tuHjXhzYOVI5jKlAYJvbIi-aUdqw'
    csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
    try:
        data = pd.read_csv(csv_url)
        data['buyer'] = data['buyer'].replace(abbreviations)
        return data
    except Exception as e:
        print("Помилка завантаження даних з Google Sheet:", e)
        return pd.DataFrame()


# Ініціалізація інтерфейсу додатку
app.layout = html.Div(children=[
    html.H1(children='Google Sheets Data Visualization'),
    dcc.Graph(id='buyer-cost-graph'),
    # Компонент для оновлення за розкладом
    dcc.Interval(
        id='interval-component',
        interval=1 * 60 * 1000,  # Оновлювати кожні 10 хвилин (у мілісекундах)
        n_intervals=0  # Стартове значення
    )
])


# Колбек для оновлення графіка
@app.callback(
    Output('buyer-cost-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n_intervals):
    # Завантажити дані
    data = load_data()
    if 'buyer' in data.columns and 'expected_cost_uah' in data.columns:
        grouped_data = data.groupby('buyer')['expected_cost_uah'].sum().reset_index()
        grouped_data = grouped_data.sort_values(by='expected_cost_uah', ascending=False)

        # Створення інтерактивного графіка за допомогою Plotly
        fig = px.bar(grouped_data,
                     x='buyer',
                     y='expected_cost_uah',
                     title='Total Expected Cost by Buyer',
                     labels={'buyer': 'Buyer', 'expected_cost_uah': 'Total Expected Cost (UAH)'})

        fig.update_layout(
            xaxis_tickangle=-45,
            width=1000,
            height=600
        )
        return fig
    else:
        # Повернути порожній графік або повідомлення про відсутність даних
        return px.scatter(title="Дані відсутні")


# Запуск сервера Dash
if __name__ == '__main__':
    app.run_server(debug=True)
