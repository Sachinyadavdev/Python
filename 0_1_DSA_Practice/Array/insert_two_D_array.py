import numpy as np

# Two D Array has been created using the Numpy Library

array2D = np.array([[12,23,56],[89,56,24],[54,26,69]])
print(array2D)

new2Darray = np.insert(array2D, 0,[25,2,2],axis=1)

print(new2Darray)