# 2D (3,4)

import numpy as np
a=np.array([[1,2,3,4],[4,5,3,6],[7,9,8,0]])
print(a)
# print(a.shape)
# order change (3,4) --->   (4,3)
# reshape()  : reshape() function is used to change the order of a matrix
b=a.reshape([4,3])
print(b)



# c=a.reshape([4,5])
# print(c)
# cannot reshape into 4,5 because array size of 12 cannot be change into 4,5
# same size elements only reshape   ie; (3,4)-->(4,3) can also change into (2,6) or (6,2)