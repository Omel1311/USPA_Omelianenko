# import requests
# import re
# from collections import Counter
# import pandas as pd
#
#
# def count_skills(api_url, target_skill):
#     try:
#         payload = {"skill": target_skill}
#         response = requests.get(api_url, params=payload)
#         response.raise_for_status()  # Проверка наличия ошибок HTTP
#
#         if response.ok:
#             data = response.json()
#
#             # Собираем все навыки в один список
#             all_skills = [skill.lower() for job in data for skill in
#                       re.split(r'\W+', job.get('Key Skills', '').lower())]
#
#
#             # Используем Counter для подсчета упоминаний каждого навыка
#             skill_counts = Counter(all_skills)
#
#             return skill_counts
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка во время выполнения запроса к API: {e}")
#         return None
#
#
# # Пример использования:
# api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
# target_skill = 'SQL'  # Замените на нужный ключевой навык
#
# skill_counts = count_skills(api_url, target_skill)
#
# if skill_counts is not None:
#     # Преобразование результатов в DataFrame
#     df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Count'])
#
#     # Сортировка по убыванию
#     df = df.sort_values(by='Count', ascending=False)
#
#     # Сохранение в Excel
#     df.to_excel(f'skill_counts_{target_skill.lower()}.xlsx', index=False)
#
#     print(f"Результаты для навыка '{target_skill}' сохранены в файл skill_counts_{target_skill.lower()}.xlsx:")
#     print(df)
# else:
#     print("Не удалось получить информацию о вакансиях.")
import requests
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.styles import Font


def count_skills(api_url, target_skills):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Проверка наличия ошибок HTTP

        if response.ok:
            data = response.json()

            # Создаем паттерн для разделения навыков на слова
            pattern = r'[^\w+#-]'

            # Инициализируем счетчик навыков
            skill_counts = Counter()

            for job in data:
                skills = re.split(pattern, job.get('Key Skills', '').lower())
                for skill in skills:
                    if skill in target_skills:
                        skill_counts[skill] += 1

            return skill_counts
    except requests.exceptions.RequestException as e:
        print(f"Ошибка во время выполнения запроса к API: {e}")
        return None


# Пример использования:
api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

# Список целевых навыков
target_skills = ['c', 'c#', 'c++', 'java', 'javascript', 'python', 'scala', 'oracle', 'sql server', 'mysql server',
                 'postgresql', 'mongodb']

skill_counts = count_skills(api_url, target_skills)

if skill_counts is not None:
    # Преобразование результатов в DataFrame
    df = pd.DataFrame(list(skill_counts.items()), columns=['Key Skills', 'Count'])

    # Сортировка по убыванию
    df = df.sort_values(by='Count', ascending=False)

    # Сохранение в Excel
    with pd.ExcelWriter('skill_counts.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Получаем объект workbook и добавляем стиль для заголовка
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        header_font = Font(size=26)
        for cell in worksheet["1:1"]:
            cell.font = header_font

        # Добавляем стиль для содержимого колонок
        content_font = Font(size=14)
        for col in worksheet.columns:
            for cell in col[1:]:
                cell.font = content_font

    # Отображение данных в виде столбчатой диаграммы
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Key Skills'], df['Count'], color='skyblue')
    plt.xlabel('Key Skills')
    plt.ylabel('Count')
    plt.title('Count of Key Skills')
    plt.xticks(rotation=45, ha='right')  # Поворот меток по оси X

    # Добавление подписей (labels) к столбцам
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom')

    plt.tight_layout()  # Для корректного отображения меток
    plt.show()

    print(df)
else:
    print("Не удалось получить информацию о вакансиях.")

