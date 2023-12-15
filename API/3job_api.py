import requests
import json
import pandas as pd
import requests

import requests


def get_number_of_jobs_with_skill(api_url, target_skill):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Проверка наличия ошибок HTTP

        if response.ok:
            data = response.json()

            # Фильтрация вакансий по наличию целевого навыка в поле 'Key Skills'
            jobs_with_skill = [job for job in data if
                               target_skill.lower() in job.get('Key Skills', '').lower().split('|')]

            number_of_jobs_with_skill = len(jobs_with_skill)
            return number_of_jobs_with_skill
    except requests.exceptions.RequestException as e:
        print(f"Ошибка во время выполнения запроса к API: {e}")
        return None


# Пример использования:
api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
target_skill = 'SQL'  # Замените на нужный ключевой навык

result = get_number_of_jobs_with_skill(api_url, target_skill)

if result is not None:
    print(f"Количество вакансий с ключевым навыком '{target_skill}': {result}")
else:
    print("Не удалось получить информацию о вакансиях.")

