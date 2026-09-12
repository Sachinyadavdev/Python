weights = ["10", "25", "15", "abc", "30", "20"]


try:
    weights = [int(weight) for weight in weights]
    print(weights)
except Exception as e:
    print("An error occurred:", e)

finally:
    pass