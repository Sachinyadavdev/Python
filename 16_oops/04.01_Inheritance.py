class Bird:
    def __init__(self, bird_name, bird_age, bird_type):
        self.bird_name = bird_name
        self.bird_age = bird_age
        self.bird_type = bird_type

    def get_bird_info(self):
        print(f"The Bird name is {self.bird_name} and the bird age is {self.bird_age} and the bird type is {self.bird_type}")

class Parrot(Bird):
    def get_new_parrot(self):
        print(f"This is the new Bord class")

b1 = Parrot("Parrot", 25, "Green")

b1.get_bird_info()

b1.get_new_parrot()