
class Animal:
    def __init__ (self,name):
        self.name = name
        def speak(self):
            return f"{self.name} Makes a sound"
        
class Dog(Animal):
    def __init__ (self,name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks, and is a {self.breed}"
    

Man = Dog("Buddy", "Golden Retriever")

print(Man.speak())