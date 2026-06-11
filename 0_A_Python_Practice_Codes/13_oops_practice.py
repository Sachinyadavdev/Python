# Challenge 1: The Car Blueprint
# Task: Create a class named Car.

# Inside the class, write an __init__ method (the constructor) that initializes two properties: brand and model.

# Create an object (instance) of this class for a Tesla Model 3.

# Print the object's brand and model.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving on the road")

Tesla1 = Car("Tesla","Model 3")

print(Tesla1.brand)
print(Tesla1.model)

Tesla1.drive()




# Challenge 2: Giving the Car a Voice
# Task: Expand your Car class by adding a custom method inside it.

# Add a method called drive(self).

# This method should print out a message using the car's properties, like: "The Tesla Model 3 is now driving!"

# Call this method using the object you created in Challenge 1.


# Challenge 3: The Bank Account (Data Encapsulation)
# Task: Create a class called BankAccount.

# The constructor __init__ should take an argument for the owner_name and set an initial property balance = 0.

# Add a method called deposit(self, amount) that adds money to the balance and prints the new balance.

# Add a method called withdraw(self, amount) that subtracts money from the balance.

# Bonus Condition: Inside withdraw, add an if statement to check if there is enough money. If amount > balance, print "Insufficient funds!" instead of subtracting.

class BankAccount:
    def __init__(self, user_name):
        self.name = user_name
        self.balance = 0

    def deposit(self, amount):
        
        if amount < 0:
            print("Invalid Amount Entered")

        else:
            self.balance = self.balance + amount

        print(f"Updated Balance is: {self.balance} " )

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient Balance")

        else:
            self.balance = self.balance - amount

        print(f"Updated Balance is: {self.balance}")

account1 = BankAccount("Sachin")

account1.deposit(10000)
account1.withdraw(100000)