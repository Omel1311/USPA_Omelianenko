import pandas as pd
import pymysql
from config import host, user, password, db_name
from sqlalchemy import create_engine


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

data = pd.read_excel('C:\\Users\\0487\\Desktop\\f.xlsx')

data=data.iloc[:,:250]
# data = data.iloc[:,:10]
print(data.head(200))

try:
     connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.Cursor)

     engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=user,
                                   pw=password,
                                   db=db_name))

     data.to_sql('3fyy', con=engine, if_exists='append')

except Exception as ex:
    print("Connection refused...")
    print(ex)
