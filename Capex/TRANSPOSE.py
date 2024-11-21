import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Чтение файла
df = pd.read_csv('C://Users//0487//Downloads//car3.csv')
print(df.head(3))

# Удаление столбца 'n'
df = df.drop(columns='n')

# Транспонирование таблицы и установка индекса
# df = df.set_index('carbody').transpose()

# Преобразование данных с помощью melt
df_melted = pd.melt(df, id_vars='carbody',
                    value_vars=['max_price', 'avg_price', 'max_difference'],
                    var_name='Price Type',
                    value_name='Price')


print(df_melted.head(3))

# Построение графика
plt.figure(figsize=(15, 10))
sns.barplot(x='carbody', y='Price', hue='Price Type', data=df_melted)
sns.lineplot(x='carbody', y='max_price', data=df, marker='o', label='Max Price')

# Линия для avg_price
sns.lineplot(x='carbody', y='avg_price', data=df, marker='o', label='Avg Price')

# Линия для max_difference
sns.lineplot(x='carbody', y='max_difference', data=df, marker='o', label='Max Difference')
# Отображение графика
plt.show()

corr = df[['max_price', 'avg_price', 'max_difference']].corr()
print(corr)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

# Настройка графика
plt.title('Correlation Heatmap of Prices and Differences')
plt.show()

