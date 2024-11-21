import pymysql
import pandas as pd
from config import host, user, password, db_name

data = pd.DataFrame({'id': [333, 5554, 666, 333, 777], 'name': ['one', 'sds', 'two', 'three', 'four']})
print(data, type(data))

# Connect to the database
try:
    connection = pymysql.connect(

        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor)

    # create cursor
    cursor=connection.cursor()
    # try:
    #     with cursor:
    #         create_table = "create table pandas_sql (id int(10), name varchar (30));"
    #         cursor.execute(create_table)
    #
    #
    # finally:
    #     connection.close()

    # creating column list for insertion
    cols = ",".join([str(i) for i in data.columns.tolist()])

    # Insert DataFrame recrds one by one.
    for i, row in data.iterrows():
        sql = "INSERT INTO pandas_sql (" +cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
        cursor.execute(sql, tuple(row))

        # the connection is not autocommitted by default, so we must commit to save our changes
        connection.commit()

    sql = "select* from pandas_sql"
    cursor.execute(sql)

    result = cursor.fetchall()
    for i in result:
        print(i)

    connection.close()


except Exception as ex:
    print("Connection refused...")
    print(ex)