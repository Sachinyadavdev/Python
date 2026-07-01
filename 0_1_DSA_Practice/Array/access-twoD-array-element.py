import numpy as np

arry2D = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arry2D)

def access_array(array, rowIndex, colIndex):
    if rowIndex>= len(arry2D) or colIndex >= len(arry2D[0]):
        print("No Such Index has been found")

    else:
        print( array[rowIndex][colIndex])
    
access_array(arry2D,2,5)