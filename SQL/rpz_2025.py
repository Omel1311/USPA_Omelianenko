import pymysql
from config import host, user, password, db_name
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor)

    print("Successfully connected...")
    print("#" * 20)

    try:
        # Отримання даних з таблиці `carprice_filtered`
        with connection.cursor() as cursor:
            count_50 = "SELECT * FROM procurement_data"
            cursor.execute(count_50)
            rows = cursor.fetchall()

            # Отримання назв колонок
            column_names = [desc[0] for desc in cursor.description]

            # Створення DataFrame з даними
            df = pd.DataFrame(rows, columns=column_names)

            # Виведення DataFrame у формі таблиці
            print(df)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)



data = pd.read_sql("SELECT * FROM procurement_data", connection)
print(data)