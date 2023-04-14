import pymysql
import pandas as pd
from config import host, user, password, db_name
from sqlalchemy import create_engine

# data = pd.DataFrame({'id': [333, 5554, 666, 333, 777], 'name': ['one', 'sds', 'two', 'three', 'four']})
# print(data, type(data))
data = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
print(type(data))

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
    data.to_sql('engine2', con=engine, if_exists='append', chunksize=1000)

except Exception as ex:
    print("Connection refused...")
    print(ex)