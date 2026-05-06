# Challenge 1: Variable Swap

a = 10
b = 5


# c = a
# a = b
# b = c

def swap(a,b):
    return b,a

print("The value of a :",a)
print("The value of b :",b)

# a,b = b,a  Pythonic login for Swapping two numbers

a,b = swap(a,b)

print(a)
print(b)