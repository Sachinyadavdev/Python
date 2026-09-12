file = open('example.txt','r')

content = "This text is written by Sachin and how we need to protect it .\n"

# file.write(content)

read_content = file.readlines()
print(read_content)
file.close()

