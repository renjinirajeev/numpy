# (5,4) matrix
# reshape into
# 4*5
# 2*10
# 1 D
# 3 D ---> (4,5)


import numpy as np
a=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[5,6,7,8],[6,7,8,9]])
print(a)
# print(a.shape)

print('-'*50)

b=a.reshape([4,5])
print(b)

print('-'*50)

c=a.reshape([2,10])
print(c)

print('-'*50)

d=a.reshape([20])
print(d)

print('-'*50)

e=a.reshape([1,4,5])
print(e)
print(e.ndim)