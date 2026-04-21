import os 

a = os.listdir("dir")
print(a)
print(os.getcwd())
print(os.path.exists("harry.txt"))
# os.remove("sample.txt")
# os.rmdir("dir")
b = os.open("harry.txt", os.O_RDWR)
print(b)