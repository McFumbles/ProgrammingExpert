class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0.0

    @property
    def balance(self):
      return round(self._balance)

    @balance.setter
    def balance(self, balance):
      
      if type(balance) == int or type(balance) == float:
        print("Balance is a number")
      
      else:
        return
      
      if balance < 0 or balance >100000:
        return
        
      self._balance = balance