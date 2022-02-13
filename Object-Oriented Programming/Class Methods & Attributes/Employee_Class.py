class Employee:
  no_employees = 0
  average_age = 0
  average_salary = 0

  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

    total_age = Employee.average_age * Employee.no_employees
    total_salary = Employee.average_salary * Employee.no_employees
    Employee.average_age = (total_age + age) / (Employee.no_employees + 1)
    Employee.average_salary = (total_salary + salary) / (Employee.no_employees + 1)
    Employee.no_employees += 1

