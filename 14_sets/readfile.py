
# f = open("data.txt", "w")
f = open("data.txt", "w")
f.write("Hello World!\n")
f.close()

f = open("data.txt", "r")
content = f.read()
print(content)
f.close()