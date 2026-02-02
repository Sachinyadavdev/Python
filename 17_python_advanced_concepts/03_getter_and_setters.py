class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ") 
        return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}" 
        self.name = new_name

e = Employee("Jack Doe", 34555)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "John"
print(e.name)

# Getter and Setter Practice 

class Student:
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        if value < 0:
            self._grade = 0
        elif value > 100:
            self._grade = 100
        else:
            self._grade = value

s = Student("Alice", 105)
print(s.grade)  # Output: 100

s.grade = -10
print(s.grade)  # Output: 0

