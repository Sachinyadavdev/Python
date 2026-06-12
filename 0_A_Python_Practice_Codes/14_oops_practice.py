# Challenge 1: The Parent Electric Vehicle
# Task: Create a parent class named Vehicle.

# The __init__ constructor should accept and assign brand and year.

# Add a method called display_info(self) that prints: "Brand: [brand], Year: [year]".



# Challenge 2: Inheriting Properties (The Child Class)
# Task: Create a child class named ElectricCar that inherits from Vehicle.

# To make a child class inherit from a parent class, put the parent class name in parentheses when defining it: class ElectricCar(Vehicle):

# Do not write any code inside ElectricCar yet; just use the keyword pass inside it.

# Create an object of ElectricCar (e.g., my_ev = ElectricCar("Tesla", 2026)).

# Call the display_info() method using your my_ev object to prove that the child class successfully stole the parent's logic!


# Challenge 3: Extending the Child Class (super())
# Task: Modify your ElectricCar child class so it has its own unique attribute that normal vehicles don't have: battery_size.

# Update the __init__ of ElectricCar to accept brand, year, AND battery_size.

# Inside its constructor, use the super().__init__(brand, year) function. This tells Python to automatically run the parent's initialization code for brand and year, saving you time!

# Manually assign the unique parameter: self.battery_size = battery_size.

# Create an object with all three parameters and print out the battery size.

# This is one of the ultimate landmarks of learning Python. Take your time setting up the parent/child link, and share your solution when you're ready!


class Vechicle:
    def __init__(self, brand, year):
        self.brand_name = brand
        self.year_name = year

    def display_info(self):
        print(f"The Brand name of the Car is {self.brand_name} and Model year is {self.year_name}")

car = Vechicle("Mercedes","2026")
car.display_info()

class ElectricCar(Vechicle):
    def __init__(self, brand, year, battery_size):
        super().__init__(brand,year)
        self.battery_size = battery_size

    def battery_info(self):
        print(f"Battery size is: {self.battery_size}")

ev = ElectricCar("Tata",2025, "1500 mah")
ev.display_info()
ev.battery_info()