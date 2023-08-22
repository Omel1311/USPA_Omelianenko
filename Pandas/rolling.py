import pandas as pd
import matplotlib.pyplot as plt

# Создаем временной ряд (пример температур)
data = {'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Temperature': [10, 12, 15, 14, 18, 20, 22, 24, 23, 25]}

df = pd.DataFrame(data)
window_size = 4  # Размер окна для скользящего среднего

# Вычисляем скользящее среднее
df['Rolling Mean'] = df['Temperature'].rolling(window=window_size).mean()

print(df)

# Визуализация
plt.plot(df['Date'], df['Temperature'], label='Temperature')
plt.plot(df['Date'], df['Rolling Mean'], label=f'Rolling Mean ({window_size}-day)')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.title('Temperature and Rolling Mean')
plt.xticks(rotation=45)
plt.show()

print(df)
