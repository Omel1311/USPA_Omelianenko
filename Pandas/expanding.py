import pandas as pd

# Создаем пример DataFrame
data = {'Value': [10, 15, 20, 25, 30]}
df = pd.DataFrame(data)

# Используем метод expanding() для вычисления накопительного среднего
df['Expanding Mean'] = df['Value'].expanding().min()
print(df)