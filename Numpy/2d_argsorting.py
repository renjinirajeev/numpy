import numpy as np
a=np.array([[5,3,4,1,2],[5,4,2,6,7],[3,7,5,8,0]])
print(a)
print(a.shape)
 #                             row wise                    column wise
 # [5,3,4,1,2]      [1 2 3 4 5]      [3 4 1 2 0]     [3 5 5]   [2 0 1]
 # [5,4,2,6,7]      [2 4 5 6 7]      [2 1 0 3 4]     [3 4 7]   [0 1 2]
 # [3,7,5,8,0]      [0 3 5 7 8]      [4 0 2 1 3]     [2 4 5]   [1 0 2]
 #                                                   [1 6 8]   [0 1 2]
 #                                                   [0,2,7]   [2 0 1]

print('-'*100)

b=np.argsort(a)            #row wise
print(b)

print('-'*100)

c=np.argsort(a,axis=0)
print(c)
#