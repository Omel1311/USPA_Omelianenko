import pandas as pd

# Загрузка Excel файла в DataFrame
file_path = 'C:\\Users\\0487\\Downloads\\Reyestr_rizikiv_black.xlsx'  # Укажите путь к вашему файлу
df = pd.read_excel(file_path)
# Удаление строк, где все значения являются пустыми
df.dropna(how='all', inplace=True)
df.to_excel('path_to_your_modified_excel_file.xlsx', index=False)