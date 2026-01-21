
class Car:

    def drive(self):
        print("Driving the vehicle")


car1 = Car()

car1.drive()

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.introduce()

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound2(self):
        print(f"The {self.species} goes '{self.sound}'")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks 'Woof Woof'")

dog1 = Dog("Dog", "Woof Woof")
dog1.make_sound()

dog1.make_sound2()