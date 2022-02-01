class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
      self.members.append(name)
    
    def delete(self, name):
      if name not in self.members:
        raise Exception("Member not in group.")
      
      else:
        self.members.remove(name)

    def get_members(self):
      return sorted(self.members)

