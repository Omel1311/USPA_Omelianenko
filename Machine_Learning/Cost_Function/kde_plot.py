import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Пример данных
data = [1, 2, 2, 3, 3, 3, 4, 4, 5,6,6,6,6,6,6,6,6,6]
data2 = [1, 3, 5, 7, 9, 11, 13, 15, 17,17,17,17,17,17,17,17,17,17]

# Построение графика KDE

max = np.argmax(data)
min = np.argmin(data)
print(max, min)
print(data[max], data[min])
sns.kdeplot(data, fill=True)
sns.kdeplot(data2, fill=True)




plt.show()
