#complex matrix

#complex numbers

# real part
# imaginary part

# a+ib

# eg :  3+5j   3 --- real , 6 ---> imaginary part


import numpy as np
a=np.array([1,3,5,6,4],dtype=complex)
print(a)


import numpy as np
a=np.array([[1+4j,2+3j,3+1j],[2+9j,4+4j,5+8j]])
print(a)
print(a.dtype)    # here it is complex with imaginary part has values.

# if we add datatype as complex in the code line imaginary part is acted as 0.
