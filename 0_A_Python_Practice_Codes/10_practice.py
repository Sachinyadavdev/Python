import compression

# Challenge 1: Squares of NumbersTask: Given a list of numbers, use a list comprehension to create a new list containing the square ($x^2$) of each number.Input List: numbers = [1, 2, 3, 4, 5]Expected Output: [1, 4, 9, 16, 25]Hint Syntax: [item * item for item in numbers]

numbers = [1,2,3,4,5]

square_num =[]

for num in numbers:
   square_num.append(num*num) 


# Python Pro Method 

cude = [num*num*num for num in numbers]

print(f"The Square of the updated list is - {square_num}")
print(f"The Cude of the updated list is - {cude}")


# Challenge 2: Filtering Even Numbers
# Task: Use a list comprehension with a built-in if condition to filter an input list and keep only the even numbers.

# Input List: numbers = [12, 5, 8, 3, 20, 15]

# Expected Output: [12, 8, 20]

# Hint: You can add an if condition at the very end of a list comprehension: [expression for item in list if condition]

all_numbers = [12,56,89,9,73,4]

even_list = [num for num in all_numbers if num%2==0]

print("The List of the Even Numbers ",even_list)

# Challenge 3: The Username Formatter
# Task: Imagine users sign up on your website, but they type their names with messy spacing and capitalization. Use a list comprehension to strip the trailing spaces and capitalize the first letter of each username.

# Input List: raw_names = [" sachin ", "AMIT", " rahul", "vijay "]

# Expected Output: ["Sachin", "Amit", "Rahul", "Vijay"]

# Hint: Python strings have built-in methods like .strip() (removes blank spaces) and .capitalize() (makes the first letter uppercase and the rest lowercase). You can chain them like name.strip().capitalize().

raw_names = ["SAHCIn", "mohan", "AMIT", " rahul", "vijay "]

clean_name = [names.strip().capitalize() for names in raw_names]

print(clean_name)

