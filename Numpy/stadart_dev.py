from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([[10], [20], [30], [40], [50]])
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

print(normalized_data)

from sklearn.preprocessing import StandardScaler

data = np.array([[10], [20], [30], [40], [50]])
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

print(standardized_data)