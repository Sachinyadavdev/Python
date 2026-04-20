numbers = [1, 2, 3, 45, 4, 21]

# def square(x):
#     return x * x 


new = list(map(lambda x: x*x, numbers))
print(new)

# Practice 

cube_numbers = [1, 2, 3, 4, 5]

def filter_cude_Numers(x):
    if x > 3:
        return True
    else:
        return False

def cube(x):
    return x * x * x

new_cubes = list(map(cube, cube_numbers))

print(new_cubes)

filtered_cubes = list(filter(filter_cude_Numers, cube_numbers))

print(filtered_cubes)


