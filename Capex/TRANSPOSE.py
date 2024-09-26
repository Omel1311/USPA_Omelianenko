import pandas as pd
import numpy as np
import sqlite3  # импорт библиотеки для работы с SQLit

df = pd.read_csv('C://Users//0487//Downloads//car3.csv')
print(df.head(3))

df = df.drop(columns='n')

df = df.set_index('carbody').transpose()

print("___________________________________")
print(df.head(3))