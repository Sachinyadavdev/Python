shipments = [
    {"id": "DEL101", "weight": 88, "delivery_days": 8},
    {"id": "DEL102", "weight": 15, "delivery_days": 3},
    {"id": "DEL103", "weight": 5, "delivery_days": 2}
]

for shipment in shipments:
    print(f"shipmentsh id : {shipment['id']}")