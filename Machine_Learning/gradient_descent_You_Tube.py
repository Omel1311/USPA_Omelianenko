from numpy.random import rand
import numpy as np
import matplotlib.pyplot as plt


def objective(x):
    return x**9.0


bounds = np.array([[-10.0, 10.0]])

inputs = []
outputs = []

for i in range(1000):
    x = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    y = objective(x)
    inputs.append(x)
    outputs.append(y)


#    функция для опередлеения градиента (скорости измененения наклона)
def derivative(x):
    return x * 2.0


result_2 = derivative(x)
print('derivative', result_2)

solutions = []
evaluations = []

for i in range(20):
    solutions.append(x)
    x_evaluation = objective(x)
    evaluations.append(x_evaluation)

    gradient = derivative(x)
    new_x = x - 0.1 * gradient
    x = new_x
    print('>%d f(%s) = %.5f' % (i, x, x_evaluation))


# plt.scatter(inputs, outputs)
# plt.scatter(solutions, evaluations, color='r')
# plt.show()


#  Отображение сразу двух граффиков
plt.figure(figsize=(10, 5))  # Задаем размер окна для графиков

# Первый график
plt.subplot(1, 3, 1)  # (количество строк, количество столбцов, индекс графика)
plt.scatter(inputs, outputs, color='blue')
plt.title('Inputs vs. Outputs')
plt.xlabel('Inputs')
plt.ylabel('Outputs')

# Второй график
plt.subplot(1, 3, 2)
plt.scatter(solutions, evaluations, color='red')
plt.title('Solutions vs. Evaluations')
plt.xlabel('Solutions')
plt.ylabel('Evaluations')


plt.subplot(1, 3, 3)
plt.scatter(inputs, outputs)
plt.scatter(solutions, evaluations, color='r')
plt.show()

# Отображение обоих графиков
plt.tight_layout()  # Эта функция помогает предотвратить перекрытие содержимого графиков
plt.show()