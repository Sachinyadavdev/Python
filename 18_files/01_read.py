# f = open("harry.txt", "r")

# content = f.read()

# print(content)

# f.close()

# Practice 

# f = open("sachin.txt", "rt")

# content = f.read()

# print(content)

# for line in f:
#     print(line)

# f.close()

# f= open("sachin.txt", "w")
f= open("sachin.txt", "a")

string = '''Sachin is aaaadddd Rahula great cricketer. He is the best batsman in the world. He has scored 100 centuries in international cricket. He is also known as the God of Cricket.'''

f.write(string)
f.close()

f2 = open("sachin.txt", "r")
content = f2.read() 
f2.close()


