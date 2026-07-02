from array import *


def find_third_largest(arr):
    n = len(arr)
    first = second = third = float('-inf')

    if n < 3:
        return -1
    
    for i in range(n):

        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second:
            third = second
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]

    return third

my_array = array('i',[25,36,6,89,100])

print(find_third_largest(my_array))