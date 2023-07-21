import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sb



url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'

df = pd.read_csv(url)
df.replace('?', np.NAN, inplace=True)

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

print(df.head())

df_gptest = df[['drive-wheels','body-style','price']]
print(df_gptest.head())

grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
print(grouped_test2.head())

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])
print("ANOVA results_total: F=", f_val, ", P =", p_val)


f_val, p_val = stats.f_oneway(  grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])
print("ANOVA results1: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])
print("ANOVA results2: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])
print("ANOVA results3: F=", f_val, ", P =", p_val)

f_val, p_val = stats.f_oneway(  grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('fwd')['price'])
p_val = np.format_float_positional(p_val, trim='-')
print("ANOVA results11: F=", f_val, ", P =", p_val)

sb.boxplot(x= 'drive-wheels', y= 'price', data=df)
plt.ylim(0,)
df.plot()
plt.show()


