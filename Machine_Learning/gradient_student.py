import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Генерируем случайные данные
np.random.seed(0)

hours_studied = np.random.randint(0, 100, 1000)
exam_scores = np.where(hours_studied < 10, np.random.randint(0, 10, 1000),
     np.where(hours_studied < 30, np.random.randint(0, 30, 1000),
     np.where(hours_studied < 50, np.random.randint(0, 80, 1000),
     np.where(hours_studied < 80, np.random.randint(0, 95, 1000),
        np.random.randint(00, 100, 1000)))))

data = {'hours_studied': hours_studied, 'exam_scores': exam_scores}
df = pd.DataFrame(data)
print(df.head())

# Функция для предсказания результатов на основе времени подготовки
def predict(hours_studied, slope, intercept):
    return slope * hours_studied + intercept


# Функция для вычисления ошибки предсказания
def compute_error(exam_scores, predicted_scores):
    return np.mean((exam_scores - predicted_scores) ** 2)


# Инициализация параметров
slope = 0
intercept = 0
learning_rate = 0.0001
num_iterations = 1000

# Градиентный спуск
for _ in range(num_iterations):
    predicted_scores = predict(hours_studied, slope, intercept)
    error = compute_error(exam_scores, predicted_scores)

    # Вычисляем градиенты
    slope_gradient = -2 * np.mean(hours_studied * (exam_scores - predicted_scores))
    intercept_gradient = -2 * np.mean(exam_scores - predicted_scores)

    # Обновляем параметры
    slope -= learning_rate * slope_gradient
    intercept -= learning_rate * intercept_gradient

    # Визуализация
    plt.scatter(hours_studied, exam_scores)
    plt.plot(hours_studied, predict(hours_studied, slope, intercept), color='red')
    plt.xlabel('Hours Studied')
    plt.ylabel('Exam Score')
    plt.title('Linear Regression using Gradient Descent')
    plt.pause(0.001)
    plt.clf()

print("Final slope:", slope)
print("Final intercept:", intercept)

