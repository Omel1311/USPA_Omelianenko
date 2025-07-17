import pandas as pd
import pymysql
from sqlalchemy import create_engine
from config import host, user, password, db_name

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

df = pd.read_excel("C:\\Users\\0487\\Downloads\\KI.xlsx", sheet_name='2026', header=[0, 1, 2])

df.columns = ['indicator_name', 'total',
              'loan_imf', 'loan_state', 'loan_banks', 'loan_total',
              'budget_funds',
              'own_amortization', 'own_profit', 'own_total',
              'other_sources',
              'branch_unit', 'department_name', 'object_group']


df.to_csv("C:\\Users\\0487\\Desktop\\KI_clean2.csv", index=False, encoding='utf-8-sig')

print(df.head(10))

# # 1. Завантаження даних з CSV
# file_path = r"C:\Users\0487\Desktop\KI_clean2.csv"
# data = pd.read_csv(file_path)
# print(data.head())

# 2. Підключення до MySQL через SQLAlchemy
try:
    # Створення SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{db_name}")

    # 3. Запис таблиці у базу (назва таблиці: chicago_schools)
    df.to_sql('ki5', con=engine, if_exists='replace', index=False)

    print("✅ Таблиця успішно створена та заповнена!")

except Exception as e:
    print("❌ Помилка підключення або запису:", e)
