import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Функция для подсчета длины слова
def word_length(word):
    return len(word)


words = ['apple', 'banana', 'cherry', 'date', 'eggfruit', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']

# Сортируем слова по убыванию длины
sorted_words = sorted(words, key=len, reverse=True)
print("Отсортированные слова по длине (убывание):")
print(" ".join(sorted_words))  # Вывод без квадратных скобок

# Создаём список кортежей (длина, слово) и сортируем по длине
length = [(len(word), word) for word in words]
sorted_length = sorted(length)

print("\nОтсортированный список (длина, слово):")
for length, word in sorted_length:
    print(f"{word}: {length}")  # Читаемый формат

# Создаём DataFrame с правильными именами колонок
df = pd.DataFrame(sorted_length, columns=['length', 'word'])

print("\nDataFrame с длинами слов:")
print(df)

word_length('apple')

sns.barplot(x='word', y='length', data=df)
plt.show()
sns.histplot(x='word', y='length', data=df)
plt.show()
sns.kdeplot(x='length', data=df)
plt.show()