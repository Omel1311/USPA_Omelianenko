import pandas as pd
import schedule
import time
import matplotlib.pyplot as plt

# Ініціалізація змінних для графіка
fig, ax = plt.subplots(figsize=(12, 8))
bars = None

def update_google_sheet():
    global bars

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

        # Оновлення графіка
        if bars is None:
            # Створення графіка (перший раз)
            bars = ax.bar(grouped_data['buyer'], grouped_data['expected_cost_uah'])
            ax.set_xlabel('Buyer')
            ax.set_ylabel('Total Expected Cost (UAH)')
            ax.set_title('Total Expected Cost by Buyer')
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.ion()  # Увімкнення інтерактивного режиму для оновлення графіка
            plt.show()
        else:
            # Оновлення висоти барів для відображення нових даних
            for bar, new_height in zip(bars, grouped_data['expected_cost_uah']):
                bar.set_height(new_height)

            # Оновлення міток по осі x, якщо список покупців змінюється
            ax.set_xticks(range(len(grouped_data)))
            ax.set_xticklabels(grouped_data['buyer'], rotation=90)

            # Оновлення фігури для відображення нових даних
            fig.canvas.draw()
            fig.canvas.flush_events()
    else:
        print("Колонки 'buyer' або 'expected_cost_uah' відсутні у завантажених даних.")

# Запланувати виконання задачі кожні 10 секунд
schedule.every(10).minutes.do(update_google_sheet)

print("Заплановано оновлення даних кожні 10 секунд.")

# Бескінечний цикл для очікування виконання задач
while True:
    schedule.run_pending()
    time.sleep(60)  # Перевіряємо кожну секунду, чи є заплановані задачі


