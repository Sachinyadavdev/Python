class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now....")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("Woof!")

# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
# print(d.location)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        print(f"Car brand: {self.brand}, Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model) # Call the parent class constructor to initialize brand and model
        self.battery_capacity = battery_capacity

    def get_info(self):
        super().get_info() # Call the parent class get_info method to print brand and model
        print(f"Battery capacity: {self.battery_capacity} kWh")

car1 = Car("Toyota", "Corolla")
car1.get_info()

ec1 = ElectricCar("Tesla", "Model 3", 75)
ec1.get_info()