import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Загружаем данные из Excel файла
file_path = 'C:\\Users\\0487\\Downloads\\RPZ.xlsx'
data = pd.read_excel(file_path)

# Суммирование стоимости по конкретным названиям предметов закупки
item_budget_distribution = data.groupby('Конкретна назва предмета закупівлі')['Загальна очікувана вартість грн. без ПДВ'].sum().sort_values(ascending=False)

# Выбираем топ-10 предметов для построения графика
top_10_items = item_budget_distribution.head(10).reset_index()

# Создание интерактивного горизонтального графика с Plotly и добавление сумм над столбцами
fig = px.bar(
    top_10_items,
    y='Конкретна назва предмета закупівлі',
    x='Загальна очікувана вартість грн. без ПДВ',
    title='Розподіл бюджету за предметами закупівлі',
    labels={
        'Конкретна назва предмета закупівлі': 'Предмет закупівлі',
        'Загальна очікувана вартість грн. без ПДВ': 'Очікувана вартість (грн. без ПДВ)'
    },
    template='plotly_white',
    orientation='h',  # Горизонтальная ориентация
    text='Загальна очікувана вартість грн. без ПДВ'  # Добавление текста над столбцами
)

fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),  # Уменьшенные отступы
    yaxis={'categoryorder':'total ascending'}  # Сортировка по сумме
)

# Создаем Dash приложение
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Розподіл бюджету за конкретною назвою предмета закупівлі', style={'textAlign': 'center'}),
    html.Div(
        dcc.Graph(figure=fig, style={'height': '90vh', 'width': '100vw'}),  # Высота 90% и ширина 100% экрана
        style={'display': 'flex', 'justifyContent': 'center', 'height': '100vh'}
    )
])

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)






