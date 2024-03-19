#dot product



import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,5])


# [1,2,3,4,5]
# [6,7,8,9,5]

# dot product   : [1*6+2*7+3*8+4*9+5*5] = 105
c=np.dot(a,b)
print(c)