# marks = [54, 23, 64, 93, 32]
# mixed = [43, "Hello", False, 4.2]

# print(marks[2:4])
# print(marks[2])
# print(mixed[4]) # Error Index out of bound


names = ["Alice", "Bob", "Rohan", 23, "Shivani"]

print(names[1:3])
print(names[3])

print(names)

names[0] = "sachin"

print(names)

while names.count("Rohan") > 0:
      names.remove("Rohan")

print(names)