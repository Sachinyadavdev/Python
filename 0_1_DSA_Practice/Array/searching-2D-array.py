import numpy as np

my_array = np.array([[25,36,14],[78,96,25],[78,45,36]])

print(my_array)

def search_array(array, value):
    
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                print(f"The value is located at {i} {j}")



    
search_array(my_array,25)



            
