import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl


pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

mpl.style.use('ggplot')  # optional: for ggplot-like style
#_______________________________________________________________
file_name ='C:\\Users\\0487\\Downloads\\Canada.csv'
df_can = pd.read_csv(file_name)
print(df_can.head())
print(df_can.info())
#_______________________________________________________________
print('*'*8300)
df_can.set_index('Country', inplace=True)
print(df_can.head())
#_______________________________________________________________
years = list(map(str, range(1980, 2014)))
print(years)
#_______________________________________________________________
print('*'*8300)

# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))
print(df_tot.head())

# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
print(df_tot.head(20))
#_______________________________________________________________
df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')
plt.show()

x = df_tot['year']      # year on x-axis
y = df_tot['total']     # total on y-axis
fit = np.polyfit(x, y, deg=1)
# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

plt.show()
