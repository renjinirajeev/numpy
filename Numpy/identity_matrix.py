# identity matrix
# diagonal elements is 1 and remaining elements is 0 then it is an identity matrix
# need to be a square matrix  ie;  no of elements in row=no of elements in column
# can only be created using 2dimension bcz its a square matrix

# [1 0 0]
# [0 1 0]
# [0 0 1]

# [1 0]
# [0 1]

# [1 0 0 0]
# [0 1 0 0]
# [0 0 1 0]
# [0 0 0 1]

import numpy as np
a=np.eye(3,dtype=int)
print(a)