import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px


# Функція для завантаження даних з Google Sheets
def column_name(col):
    sheet_id = '1QD65tuHjXhzYOVI5jKlAYJvbIi-aUdqw'
    csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
    try:
        # col = input("Введіть назву колонки: ")
        data = pd.read_csv(csv_url)
        data_unique = data[col].unique()
        for i in data_unique:
            print(i)
    except Exception as e:
        print("Помилка завантаження даних з Google Sheet:", e)
        return pd.DataFrame()

col = column_name (input("Введіть назву колонки: "))
