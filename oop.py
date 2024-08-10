# simple Atm app
class Atm:
    # method is a func written inside class
  def __init__(self):
    self.pin = ""
    self.balance = 0
    self.menu()
  def menu(self):
      user_input = input("""
       hello how would you like to proceed
        1.  enter 1 to create pin
        2.  enter 2 to deposit 
        3.  enter 3 to withdraw
        4.  enter 4 to check balance
        5.  enter 5 to exit                 """)
      if user_input == "1":
        self.create_pin()
      elif user_input == "2":
        self.deposit()
      elif user_input =="3":
        self.withdraw()
      elif user_input =="4":
        self.check_bal()
      else:
        print("exit")  
  def create_pin(self):
    self.pin = input("enter ur pin")
    print("pin set successfully")
  def deposit(self):
    temp = input("enter ur pin")
    if temp == self.pin:
      amount=int(input("enter amount to deposit"))
      self.balance =self.balance + amount
      print("successful deposit")
    else:
      print("invalid pin")
  def withdraw(self):
    temp = input("enter ur pin")
    if temp == self.pin:
      amount=int(input("enter amount to withdraw"))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print("operation successful")
      else:
        print("insufficient balance")
    else:
      print("invalid pin")
    
  def check_bal(self):
    temp = input("enter ur pin")
    if temp == self.pin:
      print(self.balance)
    else:
      print("invalid pin")

  
obj = Atm()


