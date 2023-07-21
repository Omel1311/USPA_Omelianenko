import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)


df = pd.DataFrame({'ran_num': np.random.randint(1,100,1000)})
df['bins'] = pd.cut(x=df['ran_num'], bins = [1,30,50,70,100])

print(df['bins'].value_counts())
print(df['bins'].unique())

print(df.head(100))

df.hist(column='ran_num', bins=100,grid=False, color='#FFCF56')
plt.show()