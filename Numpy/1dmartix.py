import numpy as  np
a=np.array([1,34,2,4,7,36,48,99,70,31,22])
print(a)

#argsort  : return the index number of the sorted array
# [ 1 34  2  4  7 36 48 99 70 31 22]
# [ 0  2  3  4 10  9  1  5  6  8  7]

print('-'*100)

b=np.argsort(a)
print(b)