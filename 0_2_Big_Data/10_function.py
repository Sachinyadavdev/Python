def cal_cost(weight, cost):
    total_cost = weight * cost
    return total_cost

cost = cal_cost(45,10)

print(cost)

shipments = [
    ("DEL101", 10),
    ("DEL102", 25),
    ("DEL103", 15),
    ("DEL104", 30)
]

new_shipID = []
for ship_id in shipments:
    #  print(ship_id[0])
     new_shipID.append(ship_id[0])

print(new_shipID)

new_weight = []
for weight in shipments:
    #  print(weight[1])
     new_weight.append(weight[1])

print(new_weight)


def shipment_cost(Ship_ID,Weight):
    for i in range(len(Ship_ID)):
        if Weight[i] <= 10:
            cost = Weight[i] * 20
            
        elif 10 < Weight[i] <=20:
            cost = Weight[i] *30

        elif Weight[i] > 20:
            cost = Weight[i] * 40

        # print(f"{Ship_ID[i]} : {Weight[i]} ")
        print(f"{Ship_ID[i]} : {cost} ")

shipment_cost(new_shipID, new_weight)

    

        