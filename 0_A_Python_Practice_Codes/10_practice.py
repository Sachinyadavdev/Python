# Challenge 1: Squares of NumbersTask: Given a list of numbers, use a list comprehension to create a new list containing the square ($x^2$) of each number.Input List: numbers = [1, 2, 3, 4, 5]Expected Output: [1, 4, 9, 16, 25]Hint Syntax: [item * item for item in numbers]

numbers = [1,2,3,4,5]

square_num =[]

for num in numbers:
   square_num.append(num*num) 


# Python Pro Method 

cude = [num*num*num for num in numbers]

print(f"The Square of the updated list is - {square_num}")
print(f"The Cude of the updated list is - {cude}")