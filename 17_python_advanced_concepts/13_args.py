def sum(*args): 
    # args will be a tuple of all the values passed to sum 
    total = 0
    for item in args:
        total += item 
    return total


print(sum(342, 2, 7, 9))

def multiply(*args):
    total = 1
    for item in args:
        total *= item 
    return total

print(multiply(2, 3, 4, 5))

def avearge(*args):
    total = 0
    for item in args:
        total += item
    return total/len(args)

print(avearge(9,9,9,9,9,8))