# Challenge 1: The Constant Coordinates (Tuples)
# Task: Create a tuple named location containing the latitude and longitude of a city (e.g., (13.08, 80.27)).

# Try to change the first element of the tuple to a different number (like 14.00).

# Wrap that change in a try/except block to catch the error Python throws, and print a custom message saying: "Tuples cannot be modified!"

location = (13.09, 17.23)

try:

 location[0] = 14.00

except:
  print("Tuples are immutable!")

print(location[1])

# Challenge 2: The Guest List Cleaner (Sets)
# Task: You are organizing an event and have a list of guest names, but some people accidentally registered multiple times.

# Input List: ["Sachin", "Amit", "Sachin", "Rahul", "Amit", "Vijay"]

# Task: Convert this list into a set to automatically strip away the duplicates, then print the clean collection.

names_list = ["Sachin","Ram","Amit","Rahul","Amit","Sachin","Vijay","Sohan","Ram"]

names_set = set()

for names in names_list:
  names_set.add(names)

print(names_set)

# Challenge 3: Set Operations (Common Interests)
# Task: Imagine you have two sets representing the skills of two different developers:

# Python
# dev_a = {"Python", "Git", "SQL", "Docker"}
# dev_b = {"JavaScript", "HTML", "Git", "Python"}
# Use a set method (or operator) to find out which skills they both share (Intersection).

# Use a set method (or operator) to combine their skills into a single master list of unique skills (Union).

# Take a look at how curly braces {} are used for sets without key-value pairs, and give these a shot when you're ready!

dev_a = {"Python","Java","git","sql","docker"}
dev_b = {"Javascript","HTML","Git","Python"}

dev_common = dev_a.intersection(dev_b)
dev_combine = dev_a.union(dev_b)


print(f"common skill they have {dev_common}")
print(f"common skill they have {dev_combine}")