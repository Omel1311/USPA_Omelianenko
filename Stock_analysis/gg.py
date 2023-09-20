import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']}

df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Вибір рядка, де вік більше 28
f = df.loc['b', 'Name']
print(f)