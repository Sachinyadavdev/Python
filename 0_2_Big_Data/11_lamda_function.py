square = lambda x : x*x

print(square(5))

shipments = [
    ("DEL101", 25),
    ("DEL102", 10),
    ("DEL103", 30),
    ("DEL104", 15),
    ("DEL105", 8)
]

result = sorted(shipments, key = lambda x:x[1])

print(result)