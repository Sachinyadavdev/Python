# Challenge 1: The Personalized Greeter
# Task: Write a function called greet_user(name) that takes a string parameter name and prints a welcome message.

# Example Call: greet_user("Sachin")

# Expected Output: "Hello, Sachin! Welcome back."


def greet_user(name):
    print(f"Hello, {name}! Welcome back.")

greet_user("Sachin")

# Challenge 2: Max of Three
# Task: Write a function called find_max(num1, num2, num3) that takes three numbers as arguments and returns the largest of the three.

# Constraint: Try to use if/elif/else logic inside the function instead of Python's built-in max() function to practice your logic building.

def find_max(num1, num2, num3):
    if num1 > num2 and num1>num3:
        return num1
    
    elif num3>num1 and num3>num2:
        return num3
    
    else:
        return num2
    

print(find_max(800,5,89))


# Challenge 3: List Elements MultiplierTask: Write a function called multiply_list(numbers_list) that takes a list of numbers and returns the total product (all numbers multiplied together).Example Input: [2, 3, 4]Expected Output: 24 (because $2 \times 3 \times 4 = 24$)

def multiply_list(numbers_list):
    product = 1
    for num in numbers_list:
        product *= num
    return product

numbers = [2, 3, 4]
result = multiply_list(numbers)
print(result)