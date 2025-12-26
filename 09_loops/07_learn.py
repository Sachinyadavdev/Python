# Printing the Table of the given number using the For Loop
a = int(input("Enter the number: "))

for i in range(1,11):
    print(a ,"x", i, "=", a*i)


# Iterating the List using the For loop

fruits = ["Apple","Banana","Pine Apple","Water Melon","Guava","Grapes"]

for fruit in fruits:
    print(fruit)

# While Loops 

count = 0

while count < 5:
    print("The count is: ", count)
    count +=1

# Infinite Loop2

while True:
    print("The count is: ", count)
    count +=1
