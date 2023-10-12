import pandas as pd

# 1. Устанавлииваем оптимальные опции для отображения таблиц
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# 2. считываем информацию с предоставленного Liga360 файла (тестовое задание)
file = 'C:\\Users\\0487\Desktop\\Омельяненко\\Data Science\\проект Тестовое задание 2.xlsx'
df = pd.read_excel(file, sheet_name='Old')

# 3. форматируем и очищаем данные
df.drop(39, axis=0, inplace=True)

# print(df.columns.to_list())
print(df.info())

# 4. получаем общую статистическую информацию из предоставленных данных
# (стандартное отклоненние, min, max, count, среднее и т.д.)
print(df.describe())
print(df.shape)

#  5. в ручном режиме заполняем ячейки таблицы в значении которых уверен на 100% (исходя из
#  данных в таблце о периодах оплаты)

# 6. фиксируем уровень удержания клиентов (предоставленный)
retention_rate_total = 0.96

# 7. расчитываем значение прогнозируемых значний в июле,августе 2023. Поскольку исходя их сусловий задачи следует, что
# 1) данные в таблце расчитаны по-факту (т.е. октябрь 2023)
# 2) клиенты "не новые"
# 3) и они с высокой долей веротяности "успешно" продлевались и в июле, и в августе 2023 года
# 4) то из этого следует, что на них коэфициент удержажания 0,96 с большой долей вероятности
# не распостраняется (т.к. они уже "удержаны") - оптимистический прогоноз.
# 5) поэтому в пустых ячейках за юиль и август 2023 целесообразно устанвить среднеее значение оплаты АО клиента

df['mean'] = df.loc[:, 'Лип.2023':'Сер.2024'].mean(axis=1)
df['Лип.2023'].fillna(df['mean'], inplace=True)
df['Сер.2023'].fillna(df['mean'], inplace=True)

# 8. расчитываем значение прогнозируемых значний в ноябре - декабре 2024 (сентябрь и октябрт уже предоставлен)
# c учетом уровня удержания 96%
df['Лис.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Гру.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Січ.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лют.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Бер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Кві.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Тра.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Чер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лип.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Сер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Вер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Жов.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лис.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Гру.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)

# 9. расчитываем полученную сумму и создаем в таблице 2 новые колонки - итоги
df['2023(III_Qr)'] = df[['Лип.2023', 'Сер.2023', 'Вер.2023']].sum(axis=1)
df['2024'] = df[['Січ.2024', 'Лют.2024', 'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024',
                 'Сер.2024', 'Вер.2024', 'Жов.2024', 'Лис.2024', 'Гру.2024']].sum(axis=1)

# 10. расчитываем полученную сумму по колонкам и создаем в таблице новую итоговую строку
selected_columns = ['Лип.2023', 'Сер.2023', 'Вер.2023', 'Жов.2023', 'Лис.2023', 'Гру.2023', 'Січ.2024', 'Лют.2024',
                    'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024', 'Сер.2024', '2023(III_Qr)', '2024']

df['2024'] = df[['Лип.2023', 'Сер.2023', 'Вер.2023', 'Жов.2023', 'Лис.2023', 'Гру.2023', 'Січ.2024', 'Лют.2024',
                 'Бер.2024', 'Кві.2024', 'Тра.2024', 'Чер.2024', 'Лип.2024', 'Сер.2024']].sum(axis=1)

sum_values = df[selected_columns].sum()
sum_row = pd.DataFrame([sum_values], columns=selected_columns)
df = df._append(sum_row, ignore_index=True)

# 11 вывод на екран все результатов, проврка и сверка
print(df.head())
print(df.tail())

optimistic_income = df.iloc[39, 20]
optimistic_income_rounded = round(optimistic_income, 2)

optimistic_2024 = df.iloc[39, 21]
optimistic_income_rounded_2024 = round(optimistic_2024, 2)

print("  ")
print("Итоги расчетов:(с учетом удержания клиентов)")
print("Прогнозируемый (ОПТИМИСТИЧЕКИЙ) доход компании Liga360 за III квартал 2023 года: ",
      optimistic_income_rounded, 'грн')

print("Прогнозируемый (ОПТИМИСТИЧЕКИЙ) доход компании Liga360 за 2024 год: ",
      optimistic_income_rounded_2024, 'грн')

# 12. cохраняем результаты
df.to_excel('df_optimistic_predict.xlsx', index=False)


