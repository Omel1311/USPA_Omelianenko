import pandas as pd
import pymysql
from config import host, user, password, db_name
from sqlalchemy import create_engine
import re


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)


excel_file = 'C:\\Users\\0487\\Desktop\\Омельяненко\\АНАЛІЗ_ЗП_філії\\Загальна_таблиця_ЗП.xlsx'

df=pd.read_excel(excel_file)

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor)

    # create sqlalchemy engine
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db=db_name))

    # Insert whole DataFrame into MySQL
    df.to_sql('Total_salary_table', con=engine, if_exists='append', chunksize=1000)

except Exception as ex:
    print("Connection refused...")
    print(ex)