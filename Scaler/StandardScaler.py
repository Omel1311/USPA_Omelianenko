import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Исходные данные
df = pd.DataFrame({
    'height': [150, 160, 170, 180, 190],
    'weight': [50, 60, 70, 80, 90]
})

# Стандартизация
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)
standardized_df = pd.DataFrame(standardized_data, columns=df.columns)

# Визуализация
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# До стандартизации: гистограммы
sns.histplot(df['height'], kde=False, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Height - Original')
sns.histplot(df['weight'], kde=True, ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title('Weight - Original')

# После стандартизации: гистограммы
sns.histplot(standardized_df['height'], kde=True, ax=axes[1, 0], color='orange')
axes[1, 0].set_title('Height - Standardized')
sns.histplot(standardized_df['weight'], kde=True, ax=axes[1, 1], color='red')
axes[1, 1].set_title('Weight - Standardized')

plt.tight_layout()
plt.show()
