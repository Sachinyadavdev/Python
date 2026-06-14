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