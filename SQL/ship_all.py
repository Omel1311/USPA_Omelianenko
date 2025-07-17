import pandas as pd
import pymysql
from sqlalchemy import create_engine
from config import host, user, password, db_name

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

df1 = pd.read_excel("C:\\Users\\0487\\Downloads\\2025.07.12.xlsx", skiprows=1)
df1.columns = [
    'id',
    'ship_name',
    'flag',
    'imo',
    'cargo_name',
    'cargo_quantity_tons',
    'rtk_approved_for_cargo',
    'port_operator_edsou',
    'maritime_agent_edsou',
    'freight_forwarder_edsou',
    'port_of_departure',
    'port_of_destination',
    'max_ship_length_m',
    'berth_number',
    'berth_length_m',
    'max_ship_draught',
    'average_speed_knots',
    'berth_specialization',
    'berth_in_gts_registry',
    'port_operator_in_seaport_registry'
]

df2 = pd.read_excel("C:\\Users\\0487\\Downloads\\2025.07.13.xlsx", skiprows=2)
df2.columns = df1.columns

df3 = pd.read_excel("C:\\Users\\0487\\Downloads\\2025.07.14.xlsx", skiprows=2)
df3.columns = df1.columns

df4 = pd.read_excel("C:\\Users\\0487\\Downloads\\2025.07.15.xlsx", skiprows=2)
df4.columns = df1.columns

df5 = pd.read_excel("C:\\Users\\0487\\Downloads\\2025.07.16.xlsx", skiprows=2)
df5.columns = df1.columns


df_combined = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
print(df_combined.head(1110))


# 2. Підключення до MySQL через SQLAlchemy
try:
    # Створення SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{db_name}")

    # 3. Запис таблиці у базу (назва таблиці: chicago_schools)
    df_combined.to_sql('ship_all', con=engine, if_exists='replace', index=False)

    print("✅ Таблиця успішно створена та заповнена!")

except Exception as e:
    print("❌ Помилка підключення або запису:", e)
