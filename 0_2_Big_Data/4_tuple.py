# A tuple is an ordered collection that is immutable, meaning once created, its elements cannot be changed.

shipments = [
    ("DEL101", "Delhi", "Mumbai", 12.5),
    ("DEL102", "Mumbai", "Bangalore", 8.0),
    ("DEL103", "Delhi", "Pune", 15.5),
    ("DEL104", "Delhi", "Mumbai", 10.0),
    ("DEL105", "Mumbai", "Delhi", 7.5)
]

print("Shipments in Delhi:")
for shipment in shipments:
    if shipment[1] == "Delhi":
     print(f"Shipment ID: {shipment[0]}, From: {shipment[1]}, To: {shipment[2]}, Weight: {shipment[3]} kg")
     print(f"The total Weight of shipments from Delhi is: {sum(shipment[3] for shipment in shipments if shipment[1] == 'Delhi')} kg")



