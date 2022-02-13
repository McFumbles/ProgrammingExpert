class Temperature:
  min_temperature = 0
  max_temperature = 1000

  @classmethod
  def update_min_temperature(cls, temp):
    if temp > cls.max_temperature:
      raise Exception("Invalid temperature.")

    cls.min_temperature = temp

  @classmethod
  def update_max_temperature(cls, temp):
    if temp < cls.min_temperature:
      raise Exception("Invalid temperature.")
    
    cls.max_temperature = temp

  
  def __init__(self, kelvin):
    if kelvin > self.max_temperature or kelvin < self.min_temperature:
      raise Exception("Invalid temperature.")
    
    self.kelvin = kelvin
  


