from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.datasets import load_iris

# Загружаем набор данных Iris
data = load_iris()
X = data.data
y = data.target

# Разделяем данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Задаем сетку возможных значений гиперпараметров
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'sigmoid']
}

# Создаем модель SVM
svm_model = SVC()

# Используем Grid Search CV для подбора оптимальных гиперпараметров
grid_search = GridSearchCV(svm_model, param_grid, cv=3)
grid_search.fit(X_train, y_train)

# Выводим наилучшие гиперпараметры и оценку производительности
print("Best Parameters: ", grid_search.best_params_)
print("Best Score: ", grid_search.best_score_)

# Оцениваем производительность модели на тестовом наборе данных
test_score = grid_search.score(X_test, y_test)
print("Test Score: ", test_score)
