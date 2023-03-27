import numpy as np

a = [[4,5,6], [49,5,5]]
b = [[33,4],[77,2],[7,89]]
A = np.array(a)
B = np.array(b)
R = np.dot(A,B)
print(R)
print(


)
A = np.array(a)
B = np.array(b)
print(A)
print(A.ndim)
print(A.size)
print(A.shape)

c = A[1, 1:3]
print(c)
print(


)
print(B)

print(B.T)

a=np.array([-1,1])
b=np.array([1,1])
print(np.dot(a,b))

X=np.array([[1,0,1],[2,2,2]])
out=X[0:2,2]
print(out)

X=np.array([[1,4],[0,1]])
Y=np.array([[2,1],[2,2]])
Z=np.dot(X,Y)
print('dot')

print(Z)