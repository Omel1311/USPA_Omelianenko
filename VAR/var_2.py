import pandas as pd
import numpy as np

# Завантаження Excel-файлу
file_path = 'C:\\Users\\0487\\Desktop\\22.xlsx'
data = pd.read_excel(file_path, None)

# Витяг даних із листа
df = data['Sheet1']

# Присвоєння назв колонкам для зручності
df.columns = ['fact_2019', 'fact_2020', 'fact_2021', 'fact_2022', 'fact_2023', 'fact_2024']

# Обчислення відсоткових змін між роками (доходностей)
returns = df.pct_change(axis=1).iloc[0, 1:]  # Пропускаємо перший стовпець як базовий рік

# Визначення перцентиля для 95% рівня довіри
confidence_level = 0.95
VaR_percentile = np.percentile(returns, (1 - confidence_level) * 100)

# Розрахунок VaR для кожного року від 2020 до 2027

# Створюємо список для зберігання значень VaR
VaR_results = {}

# Додаємо фактичні значення для 2020–2024 років
for year in range(2020, 2025):
    VaR_results[year] = df[f'fact_{year}'][0]

# Фактичні дані за 2024 рік
fact_2024 = df['fact_2024'][0]

# Прогнозування VaR для 2025, 2026 і 2027 років
VaR_results[2025] = fact_2024 * (1 + VaR_percentile)
VaR_results[2026] = VaR_results[2025] * (1 + VaR_percentile)
VaR_results[2027] = VaR_results[2026] * (1 + VaR_percentile)

# Виведення результатів
for year in range(2020, 2028):
    print(f"VaR для {year} року: {VaR_results[year]:.2f}")