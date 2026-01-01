# Problem 1

fruits = ['apple', 'banana', 'cherry', 'date']

print(fruits[0])

print(fruits)

fruits[1] = 'orange'

print(fruits)  # ['apple', 'orange', 'cherry', 'date']

print(len(fruits))

# Problem 2

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers)

print(numbers[0:3])

print(numbers[4:])

#Problem 3

num = [5,6,2,8,1,4,0]


print(num)

num.append(10)

print(num)  # [0, 1, 2, 4, 5, 6, 8, 10]

num.remove(2)
num.sort()
print(num)

name = ['Alice', 'Bob', 'Charlie', 'David']

name.append('Eve')

name.insert(0, 'Zara')

print(name)

# Tuples in Python

coordinates = (10, 20)

# coordinates[0] = 15  # This will raise a TypeError



print(coordinates)  # 10

# Problem 4

# convert tuple to list

coord_list = list(coordinates)

print(coord_list)  # [10, 20]


coord_tuple = tuple(coord_list)

print(coord_tuple)  # (10, 20)

# Problem 5

my_set = {1, 2, 3, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
print(my_set)  # {1, 2, 3, 4, 5}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # {3, 4}
print(a.difference(b))   # {1, 2}

# Problem 6

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict['country'] = 'USA'  # This will add a new key-value pair
print(my_dict['name'])  # Alice
print(my_dict)
print(my_dict.keys())
print(my_dict.values())

my_dict.items()

print(my_dict.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York'), ('country', 'USA'))