import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Генерация искусственных данных
np.random.seed(42)
X = np.vstack((np.random.normal([2, 2], 0.5, (50, 2)),
               np.random.normal([6, 6], 0.5, (50, 2)),
               np.random.normal([2, 6], 0.5, (50, 2))))

# Визуализация данных
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Изначальные данные")
plt.show()

# Применение алгоритма K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Визуализация результатов кластеризации
for i in range(3):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], label=f"Cluster {i+1}")
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroids')
plt.title("Результаты кластеризации K-means")
plt.legend()
plt.show()
