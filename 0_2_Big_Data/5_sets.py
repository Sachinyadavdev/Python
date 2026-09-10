source_1 = {"DEL101", "DEL102", "DEL103", "DEL104"}
source_2 = {"DEL103", "DEL104", "DEL105", "DEL106"}

union_set = source_1.union(source_2)

print("Union of source_1 and source_2:", union_set)

intersection_set = source_1.intersection(source_2)
print("Intersection of source_1 and source_2:", intersection_set)

difference_set = source_1.difference(source_2)
print("Difference of source_1 and source_2:", difference_set)