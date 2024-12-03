import seaborn as sns
import matplotlib.pyplot as plt

# Пример данных
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
data2 = [1, 3, 5, 7, 9, 11, 13, 15, 17]

# Построение графика KDE
# sns.kdeplot(data)
sns.kdeplot(data2)
# sns.kdeplot(data, bw=0.5)


sns.swarmplot(x=data, y=data, hue=data, palette="Set2")
plt.show()
