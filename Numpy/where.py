#where
# used to search element is present or not in the array

import numpy as np
a=np.array([2,4,1,3,7,44,70,0,5,32])
print(a)

b=np.where(a==5)   #>,<,<=,>=...
print(b)
c=np.where(a>5)
print(c)