# 2d (3,4)
import numpy as np
a=np.array([[2,3,4,5],[3,2,6,9],[8,9,4,6]])
print(a)


# 1 Dimension

# b=a.reshape([12])
# print(b)

#flatten()  : used for converting the matrix into 1 D without passing total no of elements

b=a.flatten()
print(b)