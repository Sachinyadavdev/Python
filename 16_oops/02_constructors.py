class Employee: 

    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
    

class Programmer(Employee):
    def __init__(self, salary, name, bond, language):
        super().__init__(salary, name, bond) # Call the parent class constructor to initialize salary, name and bond
        self.language = language

    def get_info(self):
        super().get_info() # Call the parent class get_info method to print salary, name and bond
        print(f"The programming language is {self.language}")

e1 = Employee(34000, "John Doe", 4)
p1 = Programmer(40000, "Jane Smith", 5, "Python")
print(e1.get_salary())
e1.get_info()
print(p1.get_salary())
p1.get_info()