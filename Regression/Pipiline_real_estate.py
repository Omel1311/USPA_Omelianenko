import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from  sklearn.model_selection import train_test_split
import matplotlib
from sklearn.linear_model import Ridge
import seaborn as sb
import plotly.express as px
import mplcursors

file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df = pd.read_csv(file_name)
# Ваші попередні дані та код для побудови графіку

# Побудова графіку регресії

lm = LinearRegression()
width = 10
height = 8
plt.figure(figsize=(width, height))
sns.regplot(x="floors", y="price", data=df, scatter_kws={'color':'seagreen'}, line_kws={'color':'peru'})
plt.title('floors/price')
plt.ylim(0,)

# Отримання координат лінії регресії
x_vals = df['floors']
y_vals = lm.intercept_ + lm.coef_ * x_vals
r_squared =
# Відображення лінії регресії та анотації R^2
plt.plot(x_vals, y_vals, color='peru', label='Regression Line')
plt.annotate(f'R^2 = {r_squared:.2f}', xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12, color='blue')

plt.legend()
plt.show()

# Навчаємо модель та робимо передбачення

