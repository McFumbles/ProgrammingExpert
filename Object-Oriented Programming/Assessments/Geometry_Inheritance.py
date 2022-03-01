import math


class Polygon:
  def get_sides(self):
    raise NotImplementedError

  def get_area(self):
    raise NotImplementedError
  
  def get_perimeter(self):
    return sum(self.get_sides()) 

class Triangle(Polygon):
  
  def __init__(self, t1, t2, t3):
    self.t1 = t1
    self.t2 = t2
    self.t3 = t3

  def get_sides(self):
    return self.t1, self.t2, self.t3
  
  def get_area(self):
    return get_triangle_area(self.t1, self.t2, self.t3)

class Rectangle(Polygon):

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def get_sides(self):
    return [self.width, self.height, self.width, self.height]
  
  def get_area(self):
    return get_rectangle_area(self.width, self.height)

class Square(Rectangle):

  def __init__(self, length):
    super().__init__(length, length)


def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height

