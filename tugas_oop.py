# Encapsulation 
class Employee:
    def __init__(self, name, salary):
        self.__name = name  
        self.__salary = salary  

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__salary

# inheritance, multilevel inheritance
class Manager(Employee):  # Single inheritance
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        return f"Manager Name: {self.get_name()}, Salary: {self.get_salary()}, Department: {self.department}"

class SeniorManager(Manager):  # Multilevel inheritance
    def __init__(self, name, salary, department, years_of_experience):
        super().__init__(name, salary, department)
        self.years_of_experience = years_of_experience

    def display_info(self):  # Method overriding (Polymorphism)
        return f"Senior Manager Name: {self.get_name()}, Experience: {self.years_of_experience} years, Department: {self.department}"

# Polymorphism
def display_employee_info(employee):
    print(employee.display_info())

# Membuat object
emp1 = Manager("Alice", 5000, "IT")
emp2 = SeniorManager("Bob", 8000, "HR", 10)

display_employee_info(emp1)  # Manager
display_employee_info(emp2)  # Senior Manager

emp1.set_salary(6000)
print(f"{emp1.get_name()} new salary: {emp1.get_salary()}")
