import pandas as pd
numbers = [-1, 2, 3, 0, 5, -6, 7, 8, 9, 10]

p = [(x, y) for x in numbers for y in numbers if x+y == 6]
print(p)

df=pd.DataFrame(p, columns=['x', 'y'])
print(df)
