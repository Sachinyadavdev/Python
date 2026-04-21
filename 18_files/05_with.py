# f = open("harry.txt", "r")
# content = f.read()
# print(content)
# f.close()

# with open("harry.txt", "r") as f: # context manager
#     content = f.read()
#     print(content)
    # No need to write f.close() because file is already closed by default when using with synax

with open("sachin.txt","r") as f:
    content = f.read()
    print(content)

