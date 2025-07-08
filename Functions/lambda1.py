numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = lambda x: x * x

p=(list(map(a, numbers)))
print(p)
print(type(p))
print(type(a))

for i in numbers:
    c=(i * i)
print(type(c))