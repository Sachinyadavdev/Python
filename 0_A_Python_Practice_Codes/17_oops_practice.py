transactions = [
    {"id": 1, "item": "Laptop", "amount": 1200, "status": "completed"},
    {"id": 2, "item": "Mouse", "amount": 25, "status": "pending"},
    {"id": 3, "item": "Monitor", "amount": 300, "status": "completed"},
    {"id": 4, "item": "Keyboard", "amount": 75, "status": "completed"},
    {"id": 5, "item": "HDMI Cable", "amount": 15, "status": "failed"}
]

# Challenge 1: The Total Revenue Calculator
# Task: Loop through the transactions list and calculate the total amount of money spent on all transactions combined.

# Expected Output: 1615

total = 0
for i in range(0,transactions.__len__()):
    total = transactions[i]['amount'] + total

print(f"The total amount that has been calculated is: {total}")


# Challenge 2: The Successful Filter
# Task: Create a new list called successful_items. Loop through the transactions and add the "item" name to your new list only if its "status" is exactly "completed".

# Expected Output: ['Laptop', 'Monitor', 'Keyboard']

# Bonus: Can you write this as a single-line list comprehension?

successful_items = [items['item'] for items in transactions if items['status'] == "completed"]

print(successful_items)


# Challenge 3: The Expensive Finder
# Task: Write a script that finds and prints the dictionary of the single most expensive item in the list.

# Expected Output: {"id": 1, "item": "Laptop", "amount": 1200, "status": "completed"}

# Hint: Keep a variable like most_expensive = transactions[0] and loop through the rest, comparing the "amount" key.

# This mimics exactly what data analysts and backend developers do every day. Copy the transactions list into your environment and give these three a shot!

most_expensive = transactions[0]

for t in transactions:
    if t["amount"] > most_expensive["amount"]: 
        most_expensive = t

print(f"The most expensive item is {most_expensive['item']} and its price is {most_expensive['amount']}")