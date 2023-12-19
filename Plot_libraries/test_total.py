import pandas as pd
import numpy as np

# Задаем seed для воспроизводимости результатов
np.random.seed(44)

# Создаем случайный DataFrame 5x5
data = np.random.randint(1, 5, size=(3, 3))

# Называем строки и столбцы
columns = ['A', 'B', 'C']

# Создаем DataFrame
df = pd.DataFrame(data, columns=columns)

# Выводим DataFrame


df['total_col'] = df.sum(0)[0:3]

print(df)