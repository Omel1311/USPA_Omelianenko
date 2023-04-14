import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        with connection.cursor() as cursor:
            insert_query = "insert into products values(default, 'Alend2' , 44, 4);"
            cursor.execute(insert_query)
            connection.commit()

            print('insert_query successful')
    finally:
        connection.close()




except Exception as ex:
    print("Connection refused...")
    print(ex)


