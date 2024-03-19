# list slicing    ---------->  1 D slicing

import numpy as np
a=np.array([1,3,4,7,5,8,34,29,0,28,41])
# [ 1  3  4  7  5  8 34 29  0 28 41]

print(a[1])
print(a[2:7])            # index from 2 to 6
print(a[3:])            #index 3 to end
print(a[:7])             # index 0 to 6
print(a[:])              # whole list    start to end
print(a[1:8:2])         # 1,3,5,7
print(a[2::4])          # 2,6   4 incre until end
print(a[:9:3])          # 0,3,6

