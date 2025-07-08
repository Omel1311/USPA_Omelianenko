import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("C://Users//0487//Desktop//random_data2.xlsx")
print("*"*100)
print(df.head(10))

df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df.head(10))

df["Price"] = df["Price"].replace(np.nan, df["Price"].mean())
print(df.head(10))