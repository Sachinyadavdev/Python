shipments = [
    "DEL101",
    "DEL102",
    "DEL103",
    "DEL101",
    "DEL104",
    "DEL102",
    "DEL105",
    "DEL106",
    "DEL103"
]

new_shipments = list(set(shipments))

print("Unique Shipments:", new_shipments)
print("Number of Unique Shipments:", len(new_shipments))