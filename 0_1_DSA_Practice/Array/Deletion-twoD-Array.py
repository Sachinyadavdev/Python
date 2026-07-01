import numpy as np

# Two D Array has been created using the Numpy Library

my_array = np.array([[25,36,14],[78,96,25],[78,45,36]])

print(my_array)

newArray = np.delete(my_array, 1, axis=0)

print(newArray)