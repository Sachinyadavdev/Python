from array import *

my_array = array('i',[54,84,26,58,9,32,23])

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

print(linear_search(my_array,99))