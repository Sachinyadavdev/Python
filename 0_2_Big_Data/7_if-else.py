shipment_id = "DEL101"
weight = 88
delivery_days = 8


# | Condition                                         | Category       |
# | ------------------------------------------------- | -------------- |
# | Weight > 20 kg                                    | Heavy          |
# | Weight between 10–20 kg **and** delivery days > 3 | Delayed Medium |
# | Weight between 10–20 kg **and** delivery days ≤ 3 | Medium         |
# | Weight < 10 kg                                    | Light          |

if weight > 20:
    print("Category : Heavy")

elif (10 < weight < 20) and (delivery_days > 3):
    print("Category : Delayed Medium")

elif (10 < weight < 20) and (delivery_days <= 3):
    print("Category : Medium")

elif weight < 10:
    print("Category : Light")

else:
    print("Invalid Shipment")

