class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def first_name(self):
        l = self.name.split(" ") 
        return l[0]
        

e = Employee("Jack Doe", 34555)
firstName = e.first_name()
print(firstName)