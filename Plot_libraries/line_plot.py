import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
#_______________________________________________________________
print('*'*40)

print(df_can.head())
print('*'*40)

df_can.set_index('Country', inplace=True)
df_can.index.name = None
print(df_can.head())

#_______________________________________________________________
print('*'*300)
years = list(map(str, range(1980, 2014)))
print(years)
#_______________________________________________________________
print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style
# #_______________________________________________________________
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())
#_______________________________________________________________
# haiti.plot(kind='line')
# plt.title('Immigration from Haiti')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.show()
# #_______________________________________________________________
haiti.index = haiti.index.map(int)
haiti.plot(kind='line', color = 'green')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake.
# syntax: plt.text(x, y, label)
plt.text(1979, 3333, '2010 Earthquake') # see note below


#_______________________________________________________________
# bar for vertical bar plots
# barh for horizontal bar plots
# hist for histogram
# box for boxplot
# kde or density for density plots
# area for area plots
# pie for pie plots
# scatter for scatter plots
# hexbin for hexbin plot
df_CI = df_can.loc[['India', 'China', 'Ukraine'], years]
print(df_CI.head())
df_CI = df_CI.transpose()
print(df_CI.head())
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
c = ['blue', 'red', 'green']
df_CI.plot(kind='bar', color = c, edgecolor = 'black')
plt.text(1997, 71000, 'Ukraine' )
plt.show()

