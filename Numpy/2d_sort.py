import numpy as np
a=np.array([[2,3,4,1],[4,7,9,0],[3,4,9,2],[2,0,1,7]])
print(a)

 # [2 3 4 1]
 # [4 7 9 0]
 # [3 4 9 2]
 # [2 0 1 7]

b=np.sort(a)         #default row wise sort
print(b)


print('-'*100)


b=np.sort(a,axis=0)
print(b)


# sorting in decending order
b=np.sort(a,axis=0)[::-1]
print(b)
