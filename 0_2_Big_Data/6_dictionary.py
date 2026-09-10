shipments = {
    "DEL101": 12.5,
    "DEL102": 8.0,
    "DEL103": 15.5,
    "DEL104": 10.0,
    "DEL105": 7.5
}

for shipment_id, weight in shipments.items():
    print(f"Shipment ID: {shipment_id}, Weight: {weight} kg")
    print(f"The total Weight of all shipments is: {sum(shipments.values())} kg")
    print(f"The Keys are: {shipments.keys()}")
    