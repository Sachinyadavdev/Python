
class Animal:
    def __init__ (self,name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed

    def speak(self):
        return f"{self.name} barks, and is a {self.breed}"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the parent class
        self.color = color

    def speak(self):
        return f"{self.name} meows, and is {self.color} colored"
    
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")

print(dog.speak())  # Output: Buddy barks
print(cat.speak())  # Output: Whiskers meows

# Default Values Parameter for the Constructor

class Bird(Animal):
    def __init__ (self, name, species="Parrot"):
        super().__init__(name)
        self.species = species

    def speak(self):
        return f"{self.name} chirps, and is a {self.species}"
    
bird1 = Bird("Polly")
bird2 = Bird("Tweety", "Canary")

print(bird1.speak())  # Output: Polly chirps, and is a Parrot
print(bird2.speak())  # Output: Tweety chirps, and is a

# Testing the Code in the inheritance

# New Commit Testing 



