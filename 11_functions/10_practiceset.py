import math

# Problem 1

def greet(name):
    print("hello", name)


greet("Alice")


# Problem 2

def square(num):
    return num * num

print("The square of 5 is", square(5))

# Problem 3

def full_name(first_name, last_name):
    return first_name + " " + last_name

print("Full name is:", full_name("Sachin", "Yadav"))


# Problem 4

def cal_area(length , breadth = 10):
    return length * breadth


print("Area is: ", cal_area(5))


# Problem 5

sum = lambda x, y: x + y


print("The sum is:", sum(4, 6))


# Problem 6

num1 = [1, 2, 3, 4, 5]

squared_num = list(map(lambda x: x * x, num1))

print("Squared numbers are:", squared_num)

# problem 7

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Factorial of 5 is:", factorial(5))

# Problem 8

def sum_number(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_number(n//10)

print("Sum of digits is:", sum_number(918))

# Problem 9

num = int(input("Enter a number: "))

print("The Square of the number is: ", math.sqrt(num))
print("The value of sine is: ", math.sin(num))