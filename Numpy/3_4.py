import numpy as np
a=np.array([[1,2,3],[4,5,7],[3,7,5]])
b=np.array([[2,6,9],[3,6,1],[4,9,2]])


 # [1 2 3]      # [2 6 9]
 # [4 5 7]      # [3 6 1]
 # [3 7 5]      # [4 9 2]     element by element addition

# addition of two array element wise
c=np.add(a,b)
print(c)


#substraction of two array element wise
d=np.subtract(a,b)
print(d)


#multiplication of two array element by element
e=np.multiply(a,b)
print(e)


#division of two array element by element
f=np.divide(a,b)
print(f)


#square of all elements in the matrix
g=np.square(a)
print(g)

#square root of elements : sqrt
h=np.sqrt(a)
print(h)







