# in 2D

import numpy as np
a=np.array([[1,2,3,4,5],[2,4,5,6,7],[3,5,7,8,0]])
b=np.array([[6,4,3,5,6],[5,7,9,3,0],[5,1,1,9,7]])

# join --------->  default column wise join
c=np.concatenate((a,b))
print(c)

# row wise join
c=np.concatenate((a,b),axis=1)
print(c)