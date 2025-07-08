from sklearn.preprocessing import LabelEncoder
import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)

# Данные
df = pd.read_excel('C://Users//0487//Desktop//random_data2.xlsx')
print(df.head(10))

# Создаём объект LabelEncoder
le = LabelEncoder()

# Преобразуем значения
df['category_2'] = le.fit_transform(df['category'])

print(df.head(50))

category_dummy = pd.get_dummies(df, columns=['category'])

df = pd.concat([df, pd.get_dummies(df['category'], prefix='category')], axis=1)
print(df.head(50))

df2 = df.query('category_2 == 2 and Sales > 50' )
print(df2.head(50))
print(len(df2))

print(df['Sales'].describe())
