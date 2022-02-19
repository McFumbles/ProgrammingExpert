class Animal:

  def sleep(self):
    return "ZzzZzz"
  
  def animal_sound(self):
    raise NotImplementedError("Method not implemented.")

  def wake_up(self):
    self.animal_sound()
    return "I am awake!"
  

class Lion(Animal):
  def animal_sound(self):
    return "Roar!"
