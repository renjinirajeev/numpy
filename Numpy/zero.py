#Zero matrics

# all elements in the matrix is zero then it is zero matrix
# [0,0,0]
# [0,0,0]    (2,3)


# [0,0,0,0]   (4)

# 1d zero matrix
import numpy as np
a=np.zeros([5],dtype=int)       #default datatype---> float
print(a)
print(a.dtype)


# 2d zero matrix
import numpy as np
a=np.zeros([5,2],dtype=int)
print(a)
print(a.ndim)

#3d zero matrix   (z,x,y)
import numpy as np
a=np.zeros([1,2,4],dtype=int)
print(a)
print(a.ndim)
print(a.size)     #1*2*4=8