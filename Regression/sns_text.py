import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Пример: генерация случайных данных или загрузка ваших данных
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Price': np.random.randint(100, 500, size=100),
    'Sales': np.random.uniform(10, 100, size=100)
})

# Убедитесь, что 'Date' в формате datetime
df['Date'] = pd.to_datetime(df['Date'])

# Извлекаем название месяца полностью
df['month'] = df['Date'].dt.strftime('%B')

# Разбиение 'Sales' на 10 квантильных групп
df['Sales_bin'] = pd.qcut(df['Sales'], q=10, labels=False)
df['Price_bin'] = pd.qcut(df['Price'], q=10, labels=False)

# Установка темы
sns.set_theme(style="white")

# Создание JointGrid
g = sns.JointGrid(data=df, y="Sales", x="Price", space=0)

# Основной график - ядровая оценка плотности (без clip и с уменьшенными уровнями)
g.plot_joint(sns.kdeplot,
             fill=True, thresh=0.05, levels=10, cmap="rocket")

# Маргинальные гистограммы
g.plot_marginals(sns.histplot, color="#03051A", alpha=1, bins=10)

plt.show()


