import pymysql
import pandas as pd
from config import host, user, password, db_name
from sqlalchemy import create_engine


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

    # 1 Find the total number of crimes recorded in the CRIME table
    # with connection.cursor() as cursor:
    #     total_number = "SELECT COUNT(*) FROM chicago_crime_data;"
    #     cursor.execute(total_number)
    #     total_number_fetchall = cursor.fetchone()
    #     for i in total_number_fetchall:
    #         print('*'*40)
    #         print('total number of crimes:', i)
    #         print('*' * 40)

    # 2 List community areas with per capita income less than 11000.
    # with connection.cursor() as cursor:
    #     community_areas = "SELECT COMMUNITY_AREA_NAME, PER_CAPITA_INCOME FROM census_data where PER_CAPITA_INCOME<11000;"
    #     cursor.execute(community_areas)
    #     community_areas_fetchall = cursor.fetchall()
    #     print('*' * 40)
    #     for i in community_areas:
    #         print('community areas(<$11000) : ', i)
    #     print('*' * 40)

    #  3 List all case numbers for crimes involving minors?
    # with connection.cursor() as cursor:
    #     case_numbers = "SELECT CASE_NUMBER FROM chicago_crime_data where  PRIMARY_TYPE like('%children%');"
    #     cursor.execute(case_numbers)
    #     case_numbers = cursor.fetchall()
    #     print('*' * 40)
    #     for n, i in enumerate(case_numbers, start=1):
    #         print(n, i)
    #     print('*' * 40)


    # 4 List all kidnapping crimes involving a child?
    # with connection.cursor() as cursor:
    #     kidnapping = "SELECT CASE_NUMBER, PRIMARY_TYPE, DESCRIPTION" \
    #                    " FROM final_project_coursera.chicago_crime_data" \
    #                    " where PRIMARY_TYPE = 'KIDNAPPING';"
    #     cursor.execute(kidnapping)
    #     kidnapping_crimes = cursor.fetchall()
    #     print('*' * 40)
    #     for n, i in enumerate(kidnapping_crimes, start=1):
    #         print(n, i)
    #     print('*' * 40)

    # # 5 What kinds of crimes were recorded at schools?
    # with connection.cursor() as cursor:
    #    school_crimes = "SELECT distinct(PRIMARY_TYPE), count(PRIMARY_TYPE)" \
    #                  " FROM chicago_crime_data" \
    #                  " where LOCATION_DESCRIPTION like('%school%')" \
    #                  " group by PRIMARY_TYPE;"
    #    cursor.execute(school_crimes)
    #    school_crimes_fetchall = cursor.fetchall()
    #    print('*' * 40)
    #    for n, i in enumerate(school_crimes_fetchall, start=1):
    #      print(n, i)
    #    print('*' * 40)

    # 6 List the average safety score for each type of school.
    #  with connection.cursor() as cursor:
    #       avr_safety_score = "SELECT distinct(Type_of_School), avg(SAFETY_SCORE) FROM chicago_public_schools
    #       group by Type_of_School;"
    #       cursor.execute(avr_safety_score)
    #       avr_safety_score_fetchall = cursor.fetchall()
    #       print('*' * 40)
    #       for n, i in enumerate(avr_safety_score_fetchall, start=1):
    #         print(n,i)
    #        print('*' * 40)

    # 7  List 5 community areas with highest % of households below poverty line
    # with connection.cursor() as cursor:
    #     community_areas= "SELECT COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM census_data" \
    #                        " order by PERCENT_HOUSEHOLDS_BELOW_POVERTY desc" \
    #                        " limit 5;"
    #     cursor.execute(community_areas)
    #     community_areas_fetchall = cursor.fetchall()
    #     print('*' * 40)
    #     for n, i in enumerate(community_areas_fetchall, start=1):
    #        print(n, i)
    #     print('*' * 40)

    # 8 Which community area is most crime prone?
    # with connection.cursor() as cursor:
    #     community_areas = "SELECT COMMUNITY_AREA_NAME, count(CASE_NUMBER)" \
    #                      " FROM final_project_coursera.census_data ce, final_project_coursera.chicago_crime_data cr" \
    #                      " where ce.COMMUNITY_AREA_NUMBER = cr.COMMUNITY_AREA_NUMBER" \
    #                      " group by ce.COMMUNITY_AREA_NAME" \
    #                      " order by count(CASE_NUMBER) desc" \
    #                      " limit 1"
    #     cursor.execute(community_areas)
    #     community_areas_fetchall = cursor.fetchall()
    #     print('*' * 40)
    #     for i in community_areas_fetchall:
    #        print(i)
    #     print('*' * 40)

    # 9 Use a sub-query to find the name of the community area with highest hardship index
    with connection.cursor() as cursor:
        community_areas = "SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX" \
                          " FROM final_project_coursera.census_data" \
                          " where HARDSHIP_INDEX in " \
                          "(select max(HARDSHIP_INDEX) from final_project_coursera.census_data)"
        cursor.execute(community_areas)
        community_areas_fetchall = cursor.fetchall()
        print('*' * 40)
        for i in community_areas_fetchall:
           print(i)
        print('*' * 40)

   # 10 Use a sub-query to determine the Community Area Name with most number of crimes?
    with connection.cursor() as cursor:
        community_areas = "SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX" \
                          " FROM final_project_coursera.census_data" \
                          " where HARDSHIP_INDEX in " \
                          "(select max(HARDSHIP_INDEX) from final_project_coursera.census_data)"
        cursor.execute(community_areas)
        community_areas_fetchall = cursor.fetchall()
        print('*' * 40)
        for i in community_areas_fetchall:
           print(i)
        print('*' * 40)

except Exception as ex:
    print("Connection refused...")
    print(ex)
