import pymysql
import pandas as pd
from config import host, user, password, db_name
from sqlalchemy import create_engine


data = pd.read_csv("C:\\Users\\0487\Desktop\Омельяненко\Data Science\ChicagoPublicSchools.csv")
# data2 = data.describe()
# print(type(data))
# print(data.head())

# Connect to the database
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
    # data2.to_sql('describe_python_school3', con=engine, if_exists='append')
    # data2.to_sql('describe_python_school2', con=engine, if_exists='append')

    # какие таблицы еть в БД
    # with connection.cursor() as cursor:
    #     #table_name = "select table_name FROM information_schema.tables where table_schema='coursera';"
    #     table_name = "select table_name FROM information_schema.tables where table_schema='hr';"
    #     cursor.execute(table_name)
    #     t= cursor.fetchall()

    # какие колонки еть в таблице

    # with connection.cursor() as cursor:
    #     # table_name = "select table_name FROM information_schema.tables where table_schema='coursera';"
    #     column_name = "SELECT column_name FROM information_schema.columns where table_name ='chicagopublicschools';"
    #     cursor.execute(column_name)
    #     t = cursor.fetchall()

    with connection.cursor() as cursor:
        # table_name = "select table_name FROM information_schema.tables where table_schema='coursera';"
        el_school = "SELECT COMMUNITY_AREA_NAME, sum(COLLEGE_ENROLLMENT) FROM chicagopublicschools group by (COMMUNITY_AREA_NAME) order by sum(COLLEGE_ENROLLMENT) asc limit 5;"
        cursor.execute(el_school)
        t = cursor.fetchall()
        col = ('e', 'eee')
        for i, n in enumerate(t, start=1):
            print(i, n)

        #перевод запроса в датафрейм
        #df = pd.DataFrame(t, columns=col)

        # cохранение датафрейм в  mysql
        #df.to_sql('low_70', con=engine, if_exists='append')

except Exception as ex:
    print("Connection refused...")
    print(ex)