import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df1 = pd.read_excel("C://Users//0487//Downloads//test1.xlsx")
df6 = pd.read_excel("C://Users//0487//Downloads//test6.xlsx")
print(df1.head())
print(df6.head())
print(df1.shape)
print(df6.shape)

df1 = df1[df1['PERIOD']==202406]
print(df1.shape)


e = df1.equals(df6)
print(e)

for i in range(df1.shape[0]):
    for j in range(df6.shape[0]):
        if df1.loc[i,:].equals(df6.loc[i,:]):
            continue
        else:

            if abs(df1.loc[i, 'VALUES'] / df6.loc[i, 'VALUES'] - 1) > 0.005:
                print(df1.loc[i, 'VALUES'], '***', df6.loc[i, 'VALUES'])

