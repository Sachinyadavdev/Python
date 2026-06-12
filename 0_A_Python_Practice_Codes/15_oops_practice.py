# Challenge 1: The Digital Dice (The random Module)
# Task: Use Python's built-in random module to simulate rolling a 6-sided die.

# At the very top of your script, import the module using: import random

# Use the random.randint(a, b) function to generate and print a random whole number between 1 and 6 inclusive.


# Challenge 2: The Time Capsule (The datetime Module)
# Task: Use the built-in datetime module to display information about time.

# Import the module using: from datetime import datetime

# Use datetime.now() to get the current date and time.

# Print out just the current year.

# Challenge 3: Math Wizardry (The math Module)Task: Use the built-in math module to perform advanced calculations.Import the module.Calculate and print the square root of 144 using math.sqrt().Calculate and print the value of $5$ factorial ($5! = 5 \times 4 \times 3 \times 2 \times 1$) using math.factorial().


import random
from datetime import datetime
import math

random_num = random.randint(1,6)

print(random_num)

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(math.sqrt(144))
print(math.factorial(5))