import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

#_______________________________________________________________
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

mpl.style.use('ggplot')  # optional: for ggplot-like style
#_______________________________________________________________
file_name ='C:\\Users\\0487\\Downloads\\Canada.csv'
df_can = pd.read_csv(file_name)
print(df_can.head())
print(df_can.shape)
#_______________________________________________________________
print(df_can['2013'].head())
# np.histogram returns 2 values
count, bin_edges = np.histogram(df_can['2013'])

print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins
#_______________________________________________________________
df_can['2013'].plot(kind='hist', figsize=(8, 5), color='salmon',  xticks=bin_edges)
# add a title to the histogram
plt.title('Histogram of Immigration from 195 Countries in 2013')
# add y-label
plt.ylabel('Number of Countries')
# add x-label
plt.xlabel('Number of Immigrants')
#_______________________________________________________________
df_can.set_index('Country', inplace=True)
years = list(map(str, range(1980, 2014)))
#_______________________________________________________________
df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
print(df_t.head())
df_t.plot(kind='hist', figsize=(10, 6))
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 25)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes
df_t.plot(kind ='hist',
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen'],
          xlim=(xmin, xmax),
          stacked=True,
         )

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

