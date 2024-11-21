import pandas as pd
import schedule
import time
import plotly.express as px
import plotly.io as pio

# Функція для оновлення даних з Google Sheets і створення графіка
def update_google_sheet():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_rows', 500)

    # ID вашого Google Sheet з URL
    sheet_id = '1QD65tuHjXhzYOVI5jKlAYJvbIi-aUdqw'
    # Посилання на експорт таблиці у форматі CSV
    csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'

    # Завантаження даних у DataFrame
    try:
        data = pd.read_csv(csv_url)
    except Exception as e:
        print("Помилка завантаження даних з Google Sheet:", e)
        return

    # Виведення частини даних
    print(data.head(50))

    # Групування даних за покупцем (buyer) та підрахунок загальної очікуваної вартості (expected_cost_uah)
    if 'buyer' in data.columns and 'expected_cost_uah' in data.columns:
        grouped_data = data.groupby('buyer')['expected_cost_uah'].sum().reset_index()

        # Сортування даних за загальною вартістю для зручності візуалізації
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

        # Збереження графіка як HTML
        pio.write_html(fig, file='interactive_plot.html', auto_open=True)

    else:
        print("Колонки 'buyer' або 'expected_cost_uah' відсутні у завантажених даних.")

# Запланувати виконання задачі кожні 10 хвилин
schedule.every(1).minutes.do(update_google_sheet)

print("Заплановано оновлення даних кожні 10 хвилин.")

# Бескінечний цикл для очікування виконання задач
while True:
    schedule.run_pending()
    time.sleep(50)  # Перевіряємо кожну хвилину, чи є заплановані задачі


