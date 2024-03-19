# (3,4)

import numpy as np
a=np.array([[2,3,4,6],[3,2,4,6],[8,6,4,7]])
print(a)

# [2 3 4 6]
# [3 2 4 6]
# [8 6 4 7]
#
# b=np.sum(a)
# print(b)

# sum function used for total sum in 1d or 2d

# 2d

# axis : for row wise sum and column wise sum
# axis=0  ---->  column
# axis=1  ---->  row

b=np.sum(a,axis=0)
print(b)

c=np.sum(a,axis=1)
print(c)