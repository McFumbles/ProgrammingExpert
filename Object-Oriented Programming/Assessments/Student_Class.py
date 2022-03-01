class Student:
  
  all_student = []

  def __init__(self, name, grade):
    self.name = name
    self._grade = grade
    Student.all_student.append(self)
  
  @property 
  def grade(self):
    return self._grade
  
  @grade.setter
  def grade(self, new_grade):
    if new_grade < 0 or new_grade > 100:
      raise ValueError
    
    self._grade = new_grade
  
  @staticmethod
  def calculate_average_grade(students):
    if len(students) == 0:
      return -1

    total = 0
    for student in students:
      total += student.grade
    
    return total/len(students)
  
  @classmethod
  def get_average_grade(cls):
    return cls.calculate_average_grade(cls.all_student)
  
  @classmethod 
  def get_best_student(cls):
    best_student = None

    for student in cls.all_student:
      if best_student == None or best_student.grade < student.grade:
        best_student = student
      
    return best_student

