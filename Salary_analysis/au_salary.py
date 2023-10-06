import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import matplotlib as mpl
import seaborn as sns
from pywaffle import Waffle

excel_file = 'C:\\Users\\0487\\Desktop\\Омельяненко\\Аналіз ЗП АУ\\new_analysis.xlsx'
mpl.style.use('ggplot')  # optional: for ggplot-like style

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
mpl.style.use('ggplot')  # optional: for ggplot-like style
df = pd.read_excel(excel_file, sheet_name='bi')
print(df.head())
print(df.info())

min_salary = df[df['Посадовий оклад NEW']<25000].sort_values(by='Посадовий оклад NEW', ascending=True).head(10)
print(min_salary)


df_salary = df.groupby('Самостійний підрозділ NEW').agg({'Кількість одиниць NEW': 'sum', 'Місячний фонд оплати праці NEW' : 'sum'}).sort_values(by='Місячний фонд оплати праці NEW', ascending=False)
# df_salary.set_index('Самостійний підрозділ NEW', inplace=True)
print(df_salary.head(30))

#_______________________________________________________________
plt.figure(figsize=(15,10))
sns.barplot(x='Самостійний підрозділ NEW', y='Кількість одиниць NEW', data=df)
plt.show()
#_______________________________________________________________

# ax= df_salary.plot(kind = 'bar', x='Кількість одиниць NEW', y='Місячний фонд оплати праці NEW')
ax= df_salary.plot(kind = 'bar', rot=90)
plt.xlabel('Кількість праівників в підрозідлі')  # add to x-label to the plot
plt.ylabel('Місячний фонд оплати праці (новий)')  # add y-label to the plot
plt.title('Аналіз співвідношення кількості працівників в підрозділі / місячний фонд ЗП')  # add title to the plot

ax.legend(title='Самостійний підрозділ NEW')
plt.show()


ax=df.plot(kind='hist', y = 'Посадовий оклад NEW', bins=15)
total = len(df)
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height() / total)
    x = p.get_x() + p.get_width() / 2
    y = p.get_height()
    ax.annotate(percentage, (x, y), ha='center', va='bottom')
# plt.xlabel('Кількість праівників в підрозідлі')  # add to x-label to the plot
# plt.ylabel('Місячний фонд оплати праці (новий)')  # add y-label to the plot
plt.title('Аналіз розподілу місячного фонду ЗП (новий штат)')  # add title to the plot
plt.show()

#____plt.show()___________________________________________________________
sns.countplot(x='Кількість одиниць NEW', data=df)
plt.show()

#_______________________________________________________________
#Set up the Waffle chart figure

# fig = plt.figure(FigureClass = Waffle,
#                  rows = 20, columns = 30, #pass the number of rows and columns for the waffle
#                  values = df, #pass the data to be used for display
#                  cmap_name = 'tab20' #color scheme
#                  # legend = {'labels': [f"{k} ({v})" for k, v in zip(df_salary.index.values,df_salary.Total)],
#                  #            'loc': 'lower left', 'bbox_to_anchor':(0,-0.1),'ncol': 3}
#                  #notice the use of list comprehension for creating labels
#                  #from index and total of the dataset
#                 )

#Display the waffle chart
plt.figure(figsize=(15, 6))
ax = sns.countplot(x='Самостійний підрозділ NEW', data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=6)
plt.xlabel('Самостійний підрозділ NEW', fontsize=6)
plt.show()


print(df['Самостійний підрозділ NEW'].unique())
