import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

mpl.style.use('ggplot') # optional: for ggplot-like style


conn = sqlite3.connect("m4_survey_data.sqlite") # open a database connection

#1
# QUERY1 = "select count (*) from master"
# df1 = pd.read_sql_query(QUERY1, conn)
# print(df1.head())

QUERY1 = "select * from master"
df = pd.read_sql_query(QUERY1, conn)
# print(df.info())


# # How to list all tables
# # print all the tables names in the database
# QUERY = """
# SELECT name as Table_Name FROM
# sqlite_master WHERE
# type = 'table'
# """
# # the read_sql_query runs the sql query and returns the data as a dataframe
# df0 = pd.read_sql_query(QUERY,conn)
# print(df0.head(40))

# 2
# table_name = 'master'  # the table you wish to describe
# QUERY2 = """
# SELECT Age,COUNT(*) as count
# FROM master
# group by age
# order by age
# """
# # Execute the query and store the result in a DataFrame
# df2 = pd.read_sql_query(QUERY2, conn)



# 3
# QUERY3 = """
# SELECT sql FROM sqlite_master
# WHERE name= '{}'
# """.format(table_name)
# # Execute the query and store the result in a DataFrame
# df3 = pd.read_sql_query(QUERY3, conn)
# # Print the CREATE TABLE statement
# print(df3.iat[0, 0])


#  Histograms
# plt.figure(figsize=(10, 6))
# sns.histplot(df['ConvertedComp'], kde=True, bins=30, color='skyblue')
# plt.title('Distribution of Converted Compensation')
# plt.xlabel('Converted Compensation (USD)')
# plt.ylabel('Density')
# plt.grid(True)
# # plt.show()



# Box Plots
# plt.figure(figsize=(10, 6))
# sns.boxplot(df['Age'], color='skyblue')
# plt.title('Distribution of Age')
# plt.xlabel('Converted Compensation (USD)')
# plt.ylabel('Density')
# plt.show()




# Scatter Plots
# QUERY = """
# SELECT Age, WorkWeekHrs
# FROM master
# """
# df = pd.read_sql_query(QUERY,conn)
# x=df['Age']
# y = df['WorkWeekHrs']
# sns.regplot(x=x, y=y, scatter_kws={'color': 'darkblue'}, line_kws={'color': 'red'})
# # plt.ylim(0,200)
# # plt.xlim(0,80)
# # plt.show()



# # Bubble Plots
# QUERY = """
# SELECT Age, WorkWeekHrs, CodeRevHrs
# FROM master
# """
# df = pd.read_sql_query(QUERY,conn)
# df.head()
# ax = df.plot(kind='scatter', x='WorkWeekHrs', y='CodeRevHrs', figsize=(10, 6), color='darkblue')
# # sns.regplot(x="WorkWeekHrs", y="CodeRevHrs", data=df)
# plt.title('Age Bubbles on Code Revision Hours and Work Week Hours')
# plt.xlabel('WorkWeekHrs')
# plt.ylabel('CodeRevHrs')
# plt.xlim(0,200)
# plt.show()




# Pie Charts
# table_name = 'DatabaseDesireNextYear'
# QUERY = """
# SELECT sql FROM sqlite_master
# WHERE name= '{}'
# """.format(table_name)
#
# df = pd.read_sql_query(QUERY,conn)
# print(df.iat[0,0])
#
# QUERY = """
# SELECT DatabaseDesireNextYear, count(DatabaseDesireNextYear) as Count
# FROM DatabaseDesireNextYear
# GROUP BY DatabaseDesireNextYear
# """
# df = pd.read_sql_query(QUERY,conn)
# df.sort_values('Count', ascending=False,inplace=True)
#
# df = df.head(5)
# total = df.sum(0)[1]
#
# df['percent'] = 100 * df['Count']/total
# df.set_index('DatabaseDesireNextYear')
# print(df)
#
#
# # autopct create %, start angle represent starting point
# df['Count'].plot(kind='pie',
#                             figsize=(5, 6),
#                             autopct='%1.1f%%', # add in percentages
#                             startangle=90,     # start angle 90° (Africa)
#                             shadow=True,       # add shadow
#                             labels=df['DatabaseDesireNextYear'])
#
# plt.title('Top 5 databases that respondents wish to learn next year')
# plt.axis('equal') # Sets the pie chart to look like a circle.
#
# plt.show()


# Stacked Charts
# # your code goes here
# #step 1: get the data needed
# QUERY = """
# SELECT WorkWeekHrs, CodeRevHrs, Age
# FROM master
# """
# df_age = pd.read_sql_query(QUERY,conn)
# #print(df_age.shape)
# print(df_age.head(10))
#
# # group respondents by age and apply median() function
# df_age = df_age.groupby('Age', axis=0).median()
# #df_age = df_age[30:35]
# #print(df_age.shape)
#
# # step 2: plot data
# df_age[30:35].plot(kind='bar', figsize=(10, 6), stacked=True)
# print(df_age.head(10))
# plt.xlabel('Age') # add to x-label to the plot
# plt.ylabel('Hours') # add y-label to the plot
# plt.title('Median Hours by Age') # add title to the plot
# plt.show()


# Line Chart
# #step 1: get the data needed
# QUERY = """
# SELECT ConvertedComp, Age
# FROM master
# """
# df_comp = pd.read_sql_query(QUERY,conn)
# print(df_comp[25:30].head())
#
# # group respondents by age and apply median() function
# df_comp = df_comp.groupby('Age', axis=0).median()
# print(df_comp[25:30].head())
#
#
# # step 2: plot data
# df_comp[45:60].plot(kind='line', figsize=(10, 6), stacked=True)
#
# plt.xlabel('Age') # add to x-label to the plot
# plt.ylabel('$') # add y-label to the plot
# plt.title('Median Compensation by Age') # add title to the plot
#
# plt.show()


# Bar Chart
# your code goes here
#step 1: get the data needed
QUERY = """
SELECT MainBranch, count(MainBranch) as Count
FROM master
GROUP BY MainBranch
"""
df_main = pd.read_sql_query(QUERY,conn)
print(df_main.head())

# group respondents by age and apply median() function
#df_main = df_main.groupby('Age', axis=0).median()


# step 2: plot data
df_main.plot(kind='barh', figsize=(10, 6))

plt.xlabel('Number of Respondents') # add to x-label to the plot
plt.ylabel('Main Branch') # add y-label to the plot
plt.title('Number of Respondents by Main Branch') # add title to the plot
plt.show()


conn.close()