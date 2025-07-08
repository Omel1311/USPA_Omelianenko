import numpy as np
a = np.array([(0,2,3,8,55,5,43,66), (33,33,33,33,33,33,33,33)])
print(a.dtype.name)

b = a.ndim
print(f'b = ',b)
print(f'Standart diviation', a.std())
print(a)
print(b)
print(type(a))
print(f'size', a.size)


q = np.array([4,4,5,5,5,5,5])



print(a+3)

l = np.linspace(2,4, num=10)
print(f'l = ',l)

w = np.where(a>5,4,0)
print(w)

t = w.T
print(t)


e = np.arange(10,3)
print(e)

f = np.array([44,5])
ff = np.where(f>5,4,0)
print(ff)

# a = np.array([[1, 2], [3, 4]])


h= np.arange(40)
print(h)

c = h[::-1]
print(c)