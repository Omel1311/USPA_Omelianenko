import pandas as pd
import pymysql
from config import host, user, password, db_name
from sqlalchemy import create_engine
import re

data = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
data.dropna(inplace=True)

# percentile list
perc = [.20, .40, .60, .80]

# list of dtypes to include
include = ['object', 'float', 'int']

# calling describe method
desc = data.describe(percentiles=perc, include=include)
data_describe_chicago = data.describe(include = ['object', 'float', 'int'])

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
    desc.to_sql('describe2', con=engine, if_exists='append', chunksize=1000)

except Exception as ex:
    print("Connection refused...")
    print(ex)