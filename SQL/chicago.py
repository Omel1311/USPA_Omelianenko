import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor)

    print("successfully connected...")
    print("#" * 20)

    try:
        # with connection.cursor() as cursor:
        #     count_50 = "select * from chicago_index where hardship_index < 30 order by hardship_index desc NULLS LAST FETCH FIRST ROW ONLY"
        #     cursor.execute(count_50)
        #     connection.commit()
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row[1], row[8])

        # with connection.cursor() as cursor:
        #     max_index = "select min(hardship_index) from chicago_index"
        #     cursor.execute(max_index)
        #     connection.commit()
        #     rows1 = cursor.fetchall()
        #     print(rows)

        # with connection.cursor() as cursor:
        #     max_community_area_name = "select community_area_name from chicago_index where hardship_index = (select min(hardship_index) from chicago_index)"
        #     cursor.execute(max_community_area_name)
        #     connection.commit()
        #     rows = cursor.fetchone()
        #     print(rows, rows1)

        with connection.cursor() as cursor:
            incom_60 = "select community_area_name, per_capita_income_ from chicago_index where per_capita_income_>60000"
            cursor.execute(incom_60)
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                print(row)


    finally:
        connection.close()


except Exception as ex:
    print("Connection refused...")
    print(ex)