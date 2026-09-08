class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def getname(self):
        print(f"The name is {self.name}")


e1 = Employee('Sachin','Engineer')
e1.getname()