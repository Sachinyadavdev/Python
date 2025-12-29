# Create a list containing the table of 5


# table = []

# for i in range(1, 11):
#     table.append(5*i)

table = [5*i for i in range(1, 11)]

print(table)

table2 = []

for i in range(1,11):
    print(f"5 x {i} = {5*i}")
    table2.append(f"5 x {i} = {5*i}")


print(table2) 


table2 = [2*i for i in range(1,11)]

print(table2)