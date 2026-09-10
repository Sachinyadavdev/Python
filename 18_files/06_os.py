import os 

print(os.getcwd())
a = os.listdir("dir")
print(a)
print(os.path.exists("harry.txt"))

try:
 os.remove("sample.txt")

except:
 print("File does not exist")

try:
 os.rmdir("dir")

except:
 print("dir does not exist")

try:
 b = os.open("harry.txt", os.O_RDWR)
 print(b)

except:
 print("This file is not available")


f = open("Newfile.txt",'w')
content = "This is the New file"
f.write(content)
f.close()