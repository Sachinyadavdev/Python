# Ask the user to enter a number. Check if the number is Even or Odd and print the result.


num = input("Enter the Number You want to Evaluate: ")

num = int(num)

print(type(num))

if num % 2 == 0 :
   print("The Number is Even Number")

else:
   print("The number is and ODD Number")