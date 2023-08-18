import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
#
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

file = ('C:\\Users\\0487\\Desktop\\Омельяненко\\Рені\\РЕНІ.xlsx')
df = pd.read_excel(file)

print(df.info())

bad_columns = df.filter(like='2022').columns
df.drop(columns=bad_columns, inplace=True)


# df_melt = pd.melt(df)
# print(df_melt.head(30))
# df_melt.to_excel('2022_reni.xlsx')

df_t= df.transpose()

print(df_t.info())

df_t.to_excel('2022_reni.xlsx')
sb.histplot(df_t, kde=True)
plt.xlabel('0')
plt.ylabel('1')
# sb.set (rc = {'figure.figsize':(8, 8)})
# dataplot = sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
plt.show()