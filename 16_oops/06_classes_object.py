class Employee:

    def employee_details(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        return f"Employee Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    

e1 = Employee()
print(e1.employee_details("Sachin", 30, 70000))