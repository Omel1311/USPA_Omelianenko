"""Чистая прибыль"""

import pandas as pd

# Загрузка данных о доходах и расходах
data = pd.read_csv('финансовые_данные.csv')

# Выделение колонок с доходами и расходами
revenue = data['Выручка']
expenses = data['Расходы']

# Расчет чистой прибыли
net_profit = revenue - expenses
print("Чистая прибыль:")
print(net_profit.head())