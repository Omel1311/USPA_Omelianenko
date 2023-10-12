import pandas as pd

# 1. Устанавлииваем оптимальные опции для отображения таблиц
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# 2. считываем информацию с предоставленного Liga360 файла (тестовое задание)
file = 'C:\\Users\\0487\Desktop\\Омельяненко\\Data Science\\проект Тестовое задание 2.xlsx'
df2 = pd.read_excel(file, sheet_name='дата')

# 3. Форматируем предоставленную таблицу в более "удобный" для роботы формат
# создаем сводную таблицу (pivot Table)
print(df2.columns.to_list)
df = df2.pivot_table(values='АО грн сума', index=['New_Client_ID', 'count_month'], columns='AO month', aggfunc='sum')

# 4. получаем общую статистическую информацию из предоставленных данных
# (стандартное отклоненние, min, max, count, среднее и т.д.)
print(df.describe())
print(df.shape)
print(df.info())
# 6. фиксируем уровень удержания клиентов (предоставленный)
retention_rate_total = 0.6

# 7. расчитываем значение прогнозируемых значний c учетом уровня удержания клиентов и принимаем во внимание:
# 1) данные в таблце расчитаны по-факту (т.е. 100% инфа - октябрь 2023 включительно)
# 2) клиенты "новые"
# 3) поэтому в пустых ячейках после октября целесообразно устанвить среднеее значение оплаты АО клиента * % процент удержания клиентов

df['mean'] = df.loc[:, 'Вер.2023':'Гру.2024'].mean(axis=1)

# 8. расчитываем значение прогнозируемых значний в ноябре - декабре 2024 (сентябрь и октябрт уже предоставлен)
# c учетом уровня удержания 96%

# расчитываем среднее значение и прогонозируемые значения с учетом удержания клиентов
df['Бер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Вер.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Гру.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Жов.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Кві.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лип.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лис.2023'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Лют.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Сер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Січ.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Тра.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)
df['Чер.2024'].fillna(df['mean'] * retention_rate_total, inplace=True)

# учитываем ежемесячное прибаление 2 клиентов * 3000
new = 2 * 12 * 3000 * retention_rate_total
print(new)

## 9. расчитываем полученную сумму и создаем в таблице новую колонку - общий дополнительный доход от новых клиентов
df['Total'] = df[
    ['Бер.2024', 'Вер.2023', 'Гру.2023', 'Жов.2023', 'Кві.2024', 'Лип.2024', 'Лис.2023', 'Лют.2024', 'Сер.2024',
     'Січ.2024', 'Тра.2024', 'Чер.2024']].sum(axis=1)

# #10. расчитываем полученную сумму по колонкам и создаем в таблице новую итоговую строку
selected_columns = ['Бер.2024', 'Вер.2023', 'Гру.2023', 'Жов.2023', 'Кві.2024', 'Лип.2024', 'Лис.2023', 'Лют.2024',
                    'Сер.2024', 'Січ.2024', 'Тра.2024', 'Чер.2024', 'Total']

sum_values = df[selected_columns].sum()
sum_row = pd.DataFrame([sum_values], columns=selected_columns)
df = df._append(sum_row, ignore_index=True)
#
# 11 вывод на екран все результатов, проврка и сверка
print(df.head())
print(df.tail())
print(df.info())

new_client_income = df.iloc[39, 13] + new
new_client_income_r = round(new_client_income, 2)
#

print("  ")
print("Итоги расчетов по новым клиентам:(с учетом удержания 60% и приростом + 2 клиента)")
print("Прогнозируемый доход компании Liga360 от новых клиентов за 09.2023-08.2024 года: ",
      new_client_income_r, 'грн')

# 12. cохраняем результаты
df.to_excel('new_client_predict.xlsx', index=True)
