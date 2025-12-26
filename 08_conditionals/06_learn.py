
age = input("Enter your Age: ")

age = int(age)

if age > 18:
    print("You can drive the Car")

elif age < 18:
    print("You can apply next time")

else:
    print("Invalid Age")


# Match Case in the Python

match age:
    case 18: 
        print("Match is 18")

    case 32:
        print("Match is 32")   

    case 78:
        print("match is 78")

    case _:
        print("This is the default Match Case")         