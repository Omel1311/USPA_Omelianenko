import numpy as np
a = np.array([0,2,3,8,5,43,66])
print(a.dtype.name)

b = a.ndim
print(f'Standart diviation', a.std())
print(a)
print(b)
print(type(a))
print(a.size)
q = np.array([4,4,5,5,5,5,5])
e = np.add(a,q)

print(e)
print(a+3)

l = np.linspace(1,10, num=3)
print(l)

for x in a:
    print(x+3)