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


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_info(self):
#         print(f"Car brand: {self.brand}, Model: {self.model}")

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model) # Call the parent class constructor to initialize brand and model
#         self.battery_capacity = battery_capacity

#     def get_info(self):
#         super().get_info() # Call the parent class get_info method to print brand and model
#         print(f"Battery capacity: {self.battery_capacity} kWh")

# car1 = Car("Toyota", "Corolla")
# car1.get_info()

# ec1 = ElectricCar("Tesla", "Model 3", 75)
# ec1.get_info()

class Bird():
    def __init__(self, name, bird_sound):
        self.name = name
        self.bird_sound = bird_sound

    def bird_shout(self):
        print(f"The bird {self.name} makes the sound {self.bird_sound}")

class Parrot(Bird):
    def bird_fly(self):
        print(f"Bird is flying {self.name}")


B1 = Parrot("Parrot", "chip-chip")

B1.bird_fly()