class ContactInformation:
  def __init__(self, first_name, last_name, email, phone_number):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone_number = phone_number
    self.country = None


person1 = ContactInformation(
    "Joe", "Smith", "JoeSmith@algoexpert.io", "905-999-9999")
person2 = ContactInformation(
    "Sarah", "Jones", "SarahJones@algoexpert.io", "416-333-2134")
