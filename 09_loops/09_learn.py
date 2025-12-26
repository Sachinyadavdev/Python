
# num = int(input("enter the number: "))

# if num <0:
#     print("Number is negative")

# elif num > 0:
#     print("Number is positive")

# else:
#     print("Number is zero")

# Program 2

# age = int(input("Enter your age: "))

# if age <18:
#     print("You are not eligible to vote")

# elif age > 18:
#     print("You are eligible to vote")

# else: 
#     print("You are eligible to vote soon")


# Program 3

# num = int(input("Enter a number: "))

# if num % 2 ==0:
#     print("Number is even")

# elif num % 2 != 0:
#     print("Number is odd")

# else:
#     print("Invalid input")

# Program 4

# day = int(input("Enter day number (1-7): "))

# match day:
#     case 1:
#         print("Monaday")
#     case 2:
#         print("Tuesday")
#     case 3: 
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5: 
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid Day Number")

# Program 5

# operator = input("Enter operator (+, -, *, /): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# match operator:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":   
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/":
#         if num2 != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         else:
#             print("Error: Division by zero")
#     case _:
#         print("Invalid operator")


# Problem 6

# i =0
# sum =0
# while i < 3:
#     i = i +1
#     sum = sum +i

# print(sum)
# sum =0
# for i in range (1, 4):
#     sum = sum + i

# print("The sum is: ", sum)


# Problem 7

# for i in range (1, 5):
#     print("*"*i)


# Problem 8

# correct_password = "secure123"
# password = ""
# print("Welcome to the secure system.")
# password = input("Enter your password: ")

# if password != correct_password:
#     while password != correct_password:
#         print("Access denied")
#         password = input("Enter your password Again: ")   
#     print("Access granted")
# elif password == correct_password:
#     print("Access granted")
       

# correct_password = "secure123"
# password = ""
# print("Welcome to the secure system.")
# password = input("Enter your password: ")


# if password != correct_password:
    
#     for i in range(1, 5):
#         print("Access denied")
#         i +=1
       
#         password = input("Enter your password Again: ")  
#         if password == correct_password:
#             break 
#     print("Access granted")
# elif password == correct_password:
#     print("Access granted")


# 123

num = 12398785 

num = str(num)[::-1]

print(int(num))


num = 78

num = str (num)

num = str( print (num[1],num[0],sep="") )



