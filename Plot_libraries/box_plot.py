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
df_can.set_index('Country', inplace=True)
#______________________________________________________

years = list(map(str, range(1980, 2014)))
#_______________________________________________________________
r = (df_can.loc[['Afghanistan','Ukraine'], '1984'])
print(r)
# step 1: get the data
df_iceland = df_can.loc[['Afghanistan','Ukraine'],  years].transpose()
print(df_iceland.head(4))
df_iceland.plot(kind='box', figsize=(10, 6), vert=False)

plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot

plt.show()

#_______________________________________________________________
# multyplot
fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot). See tip below**

# Subplot 1: Box plot
df_iceland.plot(kind='box', color='blue', figsize=(20, 6), ax=ax0) # add to subplot 1
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Subplot 2: Line plot
df_iceland.plot(kind='line', figsize=(20, 6), ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()

#_______________________________________________________________
# create a list of all years in decades 80's, 90's, and 00's
# The correct answer is:
df_top15 = df_can.sort_values(['Total'], ascending=False, axis=0).head(15)
print(df_top15)
years_80s = list(map(str, range(1980, 1990)))
years_90s = list(map(str, range(1990, 2000)))
years_00s = list(map(str, range(2000, 2010)))

# slice the original dataframe df_can to create a series for each decade
df_80s = df_top15.loc[:, years_80s].sum(axis=1)
df_90s = df_top15.loc[:, years_90s].sum(axis=1)
df_00s = df_top15.loc[:, years_00s].sum(axis=1)

# merge the three series into a new data frame
new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s': df_00s})

# display dataframe
print(new_df.head(15))

