import numpy as np
k=np.array([51,2,4,0,7,84,28,29,1,45,3,30,22,6])
print(k)


# highest valuse: max() functions
b=np.max(k)
print(b)


# 2D max()

import numpy as np
a=np.array([[2,3,4,1],[4,7,9,0],[3,4,9,2],[2,0,1,7]])
b=np.max(a)
print(b)

 # [2 3 4 1]
 # [4 7 9 0]
 # [3 4 9 2]
 # [2 0 1 7]

b=np.max(a)
print(b)            # max value of the matrix
c=np.max(a,axis=1)      # row wise maximum
print(c)
d=np.max(a,axis=0)      # column wise maximum
print(d)


print("-"*100)



# min
import numpy as np
k=np.array([51,2,4,0,7,84,28,29,1,45,3,30,22,6])
b=np.min(k)
print(b)


print("-"*100)

# 2D min()

import numpy as np
r=np.array([[2,3,4,1],[4,7,9,0],[3,4,9,2],[2,0,1,7]])

b=np.min(r)
print(b)
# row wise min
b=np.min(r,axis=1)
print(b)
c=np.min(r,axis=0)
print(c)


