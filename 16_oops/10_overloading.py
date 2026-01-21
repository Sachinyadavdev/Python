
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        print(f"X is {self.x} and Y is {self.y}")
        print(f"X is {p.x} and Y is {p.y}")
        print(f"The Sum of x is {self.x + p.x} and Sum of y is {self.y + p.y}")

    def __add__(self, p):
        print(f"X is {self.x} and Y is {self.y}")
        print(f"X is {p.x} and Y is {p.y}")
        print(f"The Sum of x is {self.x + p.x} and Sum of y is {self.y + p.y}")

p1 = Point(3, 2)
p2 = Point(6, 3)

p = p1 + p2  # Calls the overloaded + operator and prints the coordinates of both points

p1.sum(p2)  # Calls the sum method and prints the coordinates of both points

