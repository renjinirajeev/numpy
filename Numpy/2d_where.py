import numpy as np
a=np.array([[1,2,3,4,5],[2,4,5,6,7],[3,5,7,8,0]])
print(a)

#  [1 2 3 4 5]
#  [2 4 5 6 7]
#  [3 5 7 8 0]

b=np.where(a==4)
print(b)

# (array([0, 1], dtype=int64), array([3, 1], dtype=int64))
# ie; 4 present in (0,3)  (1,1)