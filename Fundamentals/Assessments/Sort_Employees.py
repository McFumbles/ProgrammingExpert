def sort_employees(employees, sort_by):
  sort_indices = ["name","age","salary"]
  sort_index = sort_indices.index(sort_by)

  sorted_employees = []
  employees_copy = employees[:]

  while len(employees_copy) > 0:
    smallest_index = 0

    for i, employee in enumerate(employees_copy):
      smallest = employees_copy[smallest_index][sort_index]
      if employee[sort_index] < smallest:
        smallest_index = i

    next_employee = employees_copy[smallest_index]
    sorted_employees.append(next_employee)
    employees_copy.pop(smallest_index)

  return sorted_employees
