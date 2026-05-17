# Create a list called fruits containing "apple", "banana", and "cherry".

# Add "orange" to the end of the list.

# Change "banana" to "blueberry".

# Print the length of the list using the len() function.

fruits = ["apple","banana","cherry"]

print(fruits)

fruits.append("orange")

print(fruits)

fruits[1] = "blueberry"

print(fruits)

print(len(fruits))


# Challenge 2: The Multiplier (For Loops)Task: Use a for loop and the range() function to print the multiplication table of 5 (from $5 \times 1$ to $5 \times 10$).Expected Output:51015... and so on.

for i in range(1,11):
    print(5*i)


# Challenge 3: The Sum Collector (While Loops)
# Task: Create a script that keeps asking the user to "Enter a number to add to the total" or type "exit" to stop.

# Keep a running total variable.

# When the user types "exit", stop the loop and print the final sum.

# Hint: You'll need to convert the input to an int() only if it's not "exit".

total_sum =0

while True:

    user_input = input("Enter the number you want to add or type exit to exit the loop: ")

    if user_input == "exit":
        break

    else:
        user_input = int(user_input)
        total_sum += user_input

print(f"The total sum is: {total_sum}")
