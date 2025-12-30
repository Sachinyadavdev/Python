marks = {"harry": 34, "jack": 45, "lily": 94 }

# print(marks, type(marks))
print(marks["lily"])
marks["harry"] = 3
print(marks)

marks1 ={"Physics": 43, "Chemistry": 32, "Maths": 65, "Biology": 74,"Name":"Sachin"}

print(marks1, type(marks1))

print(marks1.keys())
print(marks1.values())
marks1.pop("Chemistry")  # removes the key-value pair with key "chemistry"
print(marks1)     