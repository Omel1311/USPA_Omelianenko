import requests
import re
from collections import Counter
import pandas as pd


def count_skills(api_url, target_skill):
    try:
        payload = {"skill": target_skill}
        response = requests.get(api_url, params=payload)
        response.raise_for_status()  # Проверка наличия ошибок HTTP

        if response.ok:
            data = response.json()

            # Собираем все навыки в один список
            all_skills = [skill.lower() for job in data for skill in
                      re.split(r'\W+', job.get('Key Skills', '').lower())]


            # Используем Counter для подсчета упоминаний каждого навыка
            skill_counts = Counter(all_skills)

            return skill_counts
    except requests.exceptions.RequestException as e:
        print(f"Ошибка во время выполнения запроса к API: {e}")
        return None


# Пример использования:
api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
target_skill = 'SQL'  # Замените на нужный ключевой навык

skill_counts = count_skills(api_url, target_skill)

if skill_counts is not None:
    # Преобразование результатов в DataFrame
    df = pd.DataFrame(list(skill_counts.items()), columns=['Skill', 'Count'])

    # Сортировка по убыванию
    df = df.sort_values(by='Count', ascending=False)

    # Сохранение в Excel
    df.to_excel(f'skill_counts_{target_skill.lower()}.xlsx', index=False)

    print(f"Результаты для навыка '{target_skill}' сохранены в файл skill_counts_{target_skill.lower()}.xlsx:")
    print(df)
else:
    print("Не удалось получить информацию о вакансиях.")
