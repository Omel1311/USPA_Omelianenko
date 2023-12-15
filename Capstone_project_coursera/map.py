import pandas as pd

# Создаем пример DataFrame
data = {'Value': [10, 20, 30, 40],
        'Multiplier': [2, 3, 4, 5]}
df = pd.DataFrame(data)

# Применяем векторизованную операцию с использованием функции map()
df['Result'] = df['Value'] * df['Multiplier'].map({2: 'A', 3: 'B', 4: 'C', 5: 'D'})

# Выводим результат
print(df)