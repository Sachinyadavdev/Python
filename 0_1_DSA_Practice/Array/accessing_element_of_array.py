from array import *

my_array = array('i',[54,84,26,58,9,32,23])

def accessing_array(array,index):
    if index >= len(array):
        print("No Element is available on this index")

    else:
        print(array[index])

accessing_array(my_array,7)