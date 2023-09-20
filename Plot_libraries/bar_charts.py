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

# step 1: get the data
df_iceland = df_can.loc['Iceland', years]
df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot

plt.show()

#_______________________________________________________________
df_iceland.plot(kind='bar', figsize=(10, 6), rot=90, color='violet')

plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',  # s: str. will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )

# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' algned.
             )
plt.savefig('test.png')
plt.show()