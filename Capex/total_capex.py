import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from matplotlib.ticker import FuncFormatter

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)


df = pd.read_excel("C://Users//0487//Downloads//capex.xlsx", sheet_name="total")
df = df.iloc[1:]
df['Найменування показника'] = df['Найменування показника'].astype(str).apply(lambda x: '\n'.join(x.split()))
df.columns = df.columns.str.strip()
print(df.head(10))
print('*'*100)

df_melted = df.melt(id_vars=['Найменування показника'],
                    value_vars=['I', 'II', 'III', 'IV'],
                    var_name='Квартал',
                    value_name='Значення')

print(df_melted.head(10))
# Set Seaborn theme
sns.set_theme(style='ticks')

# Create a bar plot
ax = sns.barplot(x='Квартал', y='Значення', hue='Найменування показника', data=df_melted, palette='pastel')
# ax = sns.boxplot(x='Квартал', y='Значення', data=df_melted)
ax = sns.violinplot(x='Квартал', y='Значення', data=df_melted, color=".25")

# Настройка меток оси X для компактного размещения
plt.xticks(rotation=0, ha='center')

#
# Добавление значений к каждому столбику
# for p in ax.patches:
#     ax.annotate(format(p.get_height(), '.0f'),
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha = 'center', va = 'center',
#                 xytext = (0, 9),
#                 textcoords = 'offset points')

# Подгонка графика
plt.tight_layout()
plt.show()
