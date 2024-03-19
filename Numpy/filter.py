#filter

import numpy as np
a=np.array([41,42,43,44,45,46,47,48,49,50])
print(a)

# above 44 elements
# b=a>44        # b is the condition
# c=a[b]        # then a[condition] ie; a[b]
# print(c)



#even numbers

b=a%2==0
c=a[b]
print(c)