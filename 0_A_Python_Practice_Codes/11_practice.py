# Challenge 1: The Bulletproof Divider
# Task: Write a function called safe_divide(a, b) that divides a by b.

# Use a try/except block to catch a ZeroDivisionError if the user tries to divide by zero, and return a friendly message like "Error: Cannot divide by zero!" instead of letting the program crash.

a = input("Enter the First Number: ")
b = input("Enter the Second Number: ")


# In the Function the Code will be reusable
def safe_division(a,b):  
    try:
        result = int(a)/int(b)
        print("Division value is: ",result)


    except Exception as e:
        print("Error",e)


safe_division(a,b)

# Challenge 2: The Integer Guarantee
# Task: Write a script that asks the user to input a whole number using input().

# Wrap the int() conversion in a try/except block. If the user types letters instead of a number (which triggers a ValueError), print "That is not a valid number!" and set the variable to a default value of 0.

num = input("Enter the Whole Number: ")

try:
    num = int(num)

except ValueError :
    print("That is not a valid number! Resetting the number to 0.")
    num = 0

print("The number is: ",num)


# Challenge 3: The Multiple Exception Net
# Task: Look at this risky snippet of code:

# Python
# my_list = [10, 20, 30]
# user_index = input("Enter an index: ")  # What if they type 'abc'?
# print(my_list[int(user_index)])         # What if they type '5' (out of range)?
# Task: Rewrite this code using a try/except block that has two separate except clauses: one specifically targeting ValueError (bad input text) and another targeting IndexError (index doesn't exist in the list).

my_list = [10,20,30]

user_index = input("Enter an index: ")

try:
    print(my_list[int(user_index)])

except IndexError:
    print(f"Number out of the index! choose the number between 0 and {len(my_list)}")

except ValueError:
    print("Enter the whole number and not the text or any decimal number!")