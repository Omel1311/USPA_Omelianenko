import pandas as pd
from sqlalchemy import create_engine
import pymysql
from config import host, user, password, db_name
from datetime import datetime
from sqlalchemy.types import DATE

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# Зчитування CSV-файлу
data = pd.read_csv(r'C:\Users\0487\Downloads\cleaned_procurement_dataset_mysql.csv')

print(data.head(50))

# Видалення пробілів та ком у стовпці expected_cost_uah
data['expected_cost_uah'] = data['expected_cost_uah'].str.replace(' ', '').str.replace(',', '.')

# Перетворення типу даних на float
data['expected_cost_uah'] = pd.to_numeric(data['expected_cost_uah'], errors='coerce').fillna(0).astype('float64')

# Створення словника для заміни українських назв місяців на числові значення
months_ua = {
    'січень': '01',
    'лютий': '02',
    'березень': '03',
    'квітень': '04',
    'травень': '05',
    'червень': '06',
    'липень': '07',
    'серпень': '08',
    'вересень': '09',
    'жовтень': '10',
    'листопад': '11',
    'грудень': '12'
}

# Функція для перетворення тексту на дату
def convert_to_date(planned_date):
    if pd.isna(planned_date):
        return None
    # Приведення до нижнього регістру та видалення зайвих пробілів
    planned_date = planned_date.lower().strip()
    for ua_month, month_num in months_ua.items():
        if ua_month in planned_date:
            planned_date = planned_date.replace(ua_month, month_num)
            break

    # Видалення "р" та зайвих пробілів
    planned_date = planned_date.replace(' р', '').strip()

    # Видалення всіх зайвих крапок, якщо такі присутні
    planned_date = planned_date.replace('.', '')

    # Додавання дня (беремо перше число місяця)
    formatted_date_str = f"01-{planned_date}"

    # Перетворення рядка в формат datetime
    try:
        return datetime.strptime(formatted_date_str, '%d-%m %Y')
    except ValueError as e:
        print(f"Помилка під час перетворення дати: {planned_date} - {e}")
        return None

# Застосування функції до колонки
data['planned_date'] = data['planned_date'].apply(convert_to_date)

# Перетворення типу datetime у формат yyyy-mm-dd для зберігання в MySQL
data['planned_date'] = pd.to_datetime(data['planned_date']).dt.date

print(data.info())

# Створення підключення до MySQL за допомогою SQLAlchemy
connection_string = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
engine = create_engine(connection_string)

# Перенесення даних у таблицю MySQL
try:
    # Заміна 'procurement_data' на назву вашої таблиці
    data.to_sql('procurement_data', con=engine, if_exists='replace', index=False, chunksize=1000, dtype={'planned_date': DATE})
    print("Дані успішно перенесено в базу даних MySQL")
except Exception as e:
    print("Помилка під час перенесення даних в MySQL:", e)


data.to_excel('procurement_data2.xlsx', index=False)