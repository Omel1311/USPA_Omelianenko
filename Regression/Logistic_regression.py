# Импортируем необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

df = pd.read_excel("C://Users//0487//Desktop//Омельяненко//ПО//Odesa1.xlsx", sheet_name='Одеса')
print(df.head())

plt.figure(figsize=(10, 6))

# ax=sns.countplot(x="Причал", data=df, hue="Портовий оператор", color='r')
ax=sns.countplot(x="Портовий оператор", data=df, color='r')
# Добавление значений к каждому столбику
# for p in ax.patches:
#     ax.annotate(format(p.get_height(), '.0f'),
#                 (p.get_x() + p.get_width() / 2., p.get_height()),
#                 ha = 'center', va = 'center',
#                 xytext = (0, 9),
#                 textcoords = 'offset points')
# ax.set_title('Графік завантаженості причалів Одеськог порту')
# ax.set_facecolor((0.898, 0.898, 0.898))
# ax.set_xlabel("Кількість портових операторів, що викорстсвуюють причал")
# ax.set_xticklabels(ax.get_xticks(), rotation=90)
# ax.set_ylabel("№ Причалу")

plt.show()


plt.figure(figsize=(10, 6))

# Count plot for port operators
ax = sns.countplot(x="Портовий оператор", data=df, color='r')

# Adding values to each bar
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 9),
                textcoords='offset points')

# Title and labels
ax.set_title('Графік завантаженості причалів Одеського порту')
ax.set_facecolor((0.898, 0.898, 0.898))
ax.set_xlabel("Кількість портових операторів, що використовують причал")

# Rotate x-axis labels to vertical
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Set ylabel
ax.set_ylabel("Кількість")

plt.tight_layout()
plt.show()