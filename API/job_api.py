import requests
import pandas as pd
import json
import re

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
# response = requests.get(api_url)
# data = response.json()
# df = pd.DataFrame(data)
# print(df.head(10))
# print(df.info())
#
# def get_number_of_jobs_with_skill(api_url, target_skill):
#     try:
#         payload = {"Location": target_skill}
#         response = requests.get(api_url, params=payload)
#         response.raise_for_status()  # Проверка наличия ошибок HTTP
#
#         if response.ok:
#             data = response.json()
#
#             # Фильтрация вакансий по наличию целевого навыка в поле 'Key Skills'
#             pattern = re.compile(r'\W+')  # Регулярное выражение для разделения по любому не-буквенно-цифровому символу
#             jobs_with_skill = [job for job in data if
#                                target_skill.lower() in pattern.split(job.get('Location', '').lower())]
#
#             number_of_jobs_with_skill = len(jobs_with_skill)
#             return number_of_jobs_with_skill
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка во   время выполнения запроса к API: {e}")
#         return None
#
#
# # Пример использования:
# api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
# target_skill = 'Python'  # Замените на нужный ключевой навык
#
# result = get_number_of_jobs_with_skill(api_url, target_skill )
#
# if result is not None :
#     print(f"Количество вакансий с ключевым навыком '{target_skill}': {result}")
# else:
#     print("Не удалось получить информацию о вакансиях.")
#
# import requests
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # API URL
# api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
#
# # Send a GET request to the API URL
# response = requests.get(api_url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON content
#     data = response.json()
#
#     # Convert the JSON data to a DataFrame
#     df = pd.DataFrame(data)
#
#     # Count occurrences of each location
#     location_counts = df['Location'].value_counts()
#
#     # Convert the value counts to a DataFrame for Seaborn plotting
#     location_df = location_counts.reset_index()
#     location_df.columns = ['Location', 'Count']
#
#     # Create a bar chart using Seaborn
#     plt.figure(figsize=(12, 6))
#     ax = sns.barplot(x='Location', y='Count', data=location_df, palette='viridis')
#     plt.title('Bar Chart of Jobs by Location (Using Seaborn)')
#     plt.xlabel('Location')
#     plt.ylabel('Count')
#     plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
#
#     # Annotate each bar with its count value and increase font size
#     for index, value in enumerate(location_df['Count']):
#         ax.text(index, value + 0.5, str(value), color='black', ha="center", fontsize=14)
#
#     plt.tight_layout()  # Adjust layout to prevent clipping
#     plt.show()
#
#     # Print DataFrame info
#     print(df.info())
# else:
#     print("Failed to retrieve data from the API.")

import pandas as pd

# Список указанных ключевых навыков
specified_skills = ['C', 'C#', 'C++', 'Java', 'JavaScript', 'Python', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB']

# Пример данных (обычно вы бы получали эти данные из вашего источника данных, например, из API)
data = {
    'Key Skills': ['Python, Java', 'C++, Java, Python', 'JavaScript, C#', 'C++, Python', 'Java', 'SQL Server, Python, C#']
}

# Создание DataFrame из данных
df = pd.DataFrame(data)

# Функция для подсчета вхождений указанных навыков в столбце 'Key Skills'
def count_skills(skill_list, skills_string):
    count = 0
    for skill in skill_list:
        if skill in skills_string:
            count += 1
    return count

# Применение функции count_skills к каждой строке столбца 'Key Skills' и сохранение результатов в новом столбце 'Count'
df['Count'] = df['Key Skills'].apply(lambda x: count_skills(specified_skills, x))

# Фильтрация DataFrame, чтобы включить только строки с ненулевым количеством указанных навыков
filtered_df = df[df['Count'] > 0]

# Отображение отфильтрованного DataFrame
print(filtered_df)


