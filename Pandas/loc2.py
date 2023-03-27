import pandas as pd
x = {'Name': ['Rose','John', 'Jane', 'Mary'],
     'ID': [1, 2, 3, 4],
     'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

x1 = pd.DataFrame(x)
print(x1)
w = x1.iloc[0,2]


print(w)