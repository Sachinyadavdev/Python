
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def employee_details(self):
        return f"Employee Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

name = input("Enter Name: ")
age = int(input("Enter Age: "))
salary = int(input("Enter Salary: "))

e1 = Employee(name, age, salary)

print(e1.employee_details())


# Testing