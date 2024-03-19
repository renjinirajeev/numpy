# 2 D slicing


import numpy as np
a=np.array([[2,4,5,3,9],[4,6,2,7,0],[4,8,6,9,1],[3,6,8,4,2]])
print(a)

 # [2 4 5 3 9]
 # [4 6 2 7 0]
 # [4 8 6 9 1]
 # [3 6 8 4 2]

 # print(a[row,columns])
print(a[1:,:3])    # row=1,2,3   , column=0,1,2
print(a[1:4,:3])   # row =1,2,3  , column=0,1,2
print(a[2:,2:4])   # row =2,3  , column= 2,3
print(a[:3,1:3])   # row = 0,1,2  column=1,2
print(a[1:4:2,2::2])


# zeroth row of data
# print(a[0:1,0:5])
print(a[0,:])


# zeroth column of data
# print(a[0:4,0:1])
print(a[:,0])