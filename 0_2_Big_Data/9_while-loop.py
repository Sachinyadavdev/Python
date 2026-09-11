i = 0
while i < 15:
    print("The Value of i after the increment is: ",i)
    i = i+1

weights = [5, 12, 25, 8, 30, 15, 7, 22]

n = 0
heavy_weight = 0
for weight in weights:
    if weight > 20:
        n = n + 1
        heavy_weight = heavy_weight + weight

print(f"The Total weight greater then 20 is {n}")
print(f"The Total Heavy Weight is : {heavy_weight}")