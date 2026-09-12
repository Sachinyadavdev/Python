# by using the with we don't need to close the file using the close()

with open('example.txt','r') as file:
    content =file.read()
    print(content)


