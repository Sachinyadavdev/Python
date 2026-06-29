from array import *

def find_second_largest(arr):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num>largest:
            second_largest = largest
            largest = num

        elif num>second_largest and num!= largest:
            second_largest = num

    if second_largest == float('-inf'):
        return -1
    
    return second_largest

my_array = array('i',[90,90])

print(find_second_largest(my_array))
