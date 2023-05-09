import pymysql
import pandas as pd
from config import host, user, password, db_name
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns


# data = pd.DataFrame({'id': [333, 5554, 666, 333, 777], 'name': ['one', 'sds', 'two', 'three', 'four']})
# print(data, type(data))
data = pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')

data.plot.scatter(x=3,y=33)
plt.show()
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
    data.dropna(inplace=True)
    data.to_sql('engine2', con=engine, if_exists='append', chunksize=1000)

    with connection.cursor() as cursor:
        income_vs_hardship = data.iloc[8:9]
        income_vs_hardship = pd.read_sql_query("select per_capita_income_, hardship_index from  ")
        cursor.execute(income_vs_hardship)
        connection.commit()
        plot = sns.jointplot(x='per_capita_income_', y='hardship_index', data=income_vs_hardship.DataFrame())
        plt.show
except Exception as ex:
    print("Connection refused...")
    print(ex)