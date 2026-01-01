list1 = [1,2,2,3,4,4,5,5,5]

print(list1)

unique_list = list(set(list1))

print(unique_list)

product_price = {"Car":10000, "Bike":5000, "Bus":20000, "Truck":30000}

most_expensive = max(product_price)

print("Most expensive product:", most_expensive)  # Truck

product_price2 = {"cycle":800, "scooter":1500, "skateboard":300}

combine_prices = {**product_price, **product_price2}

print("Combined product prices:", combine_prices)