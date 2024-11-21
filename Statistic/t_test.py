import numpy as np
from scipy import stats

# Генерация случайных данных (рост мужчин и женщин)
group1 = np.random.normal(loc=175, scale=10, size=100)  # рост мужчин
group2 = np.random.normal(loc=165, scale=10, size=100)  # рост женщин

print(group1)
print(group2)

[]
# Проведение t-теста для двух выборок
t_stat, p_value = stats.ttest_ind(group1, group2)

print("t-статистика:", (format(t_stat, '.20f')  ))
print("p-значение:", (format(p_value, '.20f')))


