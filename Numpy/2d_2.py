import numpy as np
a=np.array([[1,2,3,4,5],[2,4,5,6,7],[3,5,7,8,0]])
print(a)


# argmax() :

# default maximum element in the matrix (not row wise or column wise)

b=np.argmax(a)
print(b)

print('-'*100)

# row wise
b=np.argmax(a,axis=1)
print(b)


print('-'*100)
# column wise
b=np.argmax(a,axis=0)
print(b)



print('-'*100)

# agrmin()

b=np.argmin(a)
print(b)


print('-'*100)

# row wise argmin
b=np.argmin(a,axis=1)
print(b)


print('-'*100)

#column wise argmin
b=np.argmin(a,axis=0)
print(b)

