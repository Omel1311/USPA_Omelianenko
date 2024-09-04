import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

df1 = pd.read_excel("C://Users//0487//Downloads//applications_test_1.xlsx")
df6 = pd.read_csv("C://Users//0487//Downloads//applications_test_6.csv")

print(df6.shape)

# df66 = df6.to_excel('applications_test_6.xlsx')

df6 = df6[df6['PERIOD']==202406]
print(df6.head())
print(df6.head())

print(df1.shape)
print(df6.shape)

for i in range(df1.shape[0]):
    if df1.loc[i, :].equals(df6.loc[i ,:]):
        print('same')
    else:
        print('not same')


    # else:
    #     # if abs(df1.loc[i, 'VALUES'] / df6.loc[i, 'VALUES'] - 1) < 0.005:
    #        print(df1.loc[i, 'VALUES'], '***', df6.loc[i, 'VALUES'])
    # #
