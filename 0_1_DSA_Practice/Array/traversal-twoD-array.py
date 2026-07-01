import numpy as np

array2D = np.array([[1,2,3],[45,23,9],[89,25,6]])

print(array2D)

def traversal_arr(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traversal_arr(array2D)