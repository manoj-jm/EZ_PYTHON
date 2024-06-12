#bank account file

class BalanceException(Exception):
  pass

class BankAccount:
  def __init__(self,initialAmt , accName) -> None:
    self.balance = initialAmt
    self.name = accName
    
  def getBalance(self):
    print(f"\nAccount {self.name} Balance = RS {self.balance:.2f} ")

  def deposite(self,amt):
    self.balance = self.balance + amt
    print("Deposit complete")
    self.getBalance()

  def viableTransaction(self,amt):
    if self.balance>=amt:
      return
    else:
      raise BalanceException(f"\nSorry,account '{self.name}' has only balance amount of '{self.balance:.2f}'")
    
  def withDraw(self,amt):
    try:
      self.viableTransaction(amt)
      self.balance = self.balance -amt
      print("withdraw complete")
      self.getBalance()
    except BalanceException as error:
      print("interrupted transaction " , error)

  def transferAmt(self,sendAmt,receiverAccount):
    try:
      print('********************\nBeginning Transfer ...')
      self.viableTransaction(sendAmt)
      self.withDraw(sendAmt)
      receiverAccount.deposite(sendAmt)
      print("Transfer Completed ********************✅ ")
    except BalanceException as error:
      print("Interrupted Transfer ❌")
      
      self.viableTransaction(sendAmt)
      
    
    

class InterestRewardAcct(BankAccount):
  def deposite(self, amt):
    self.balance = self.balance + (amt * 1.05)
    print("Deposite Complete ")
    self.getBalance()


class SavingAcct(InterestRewardAcct):
  def __init__(self,initialamt,accName):
    super().__init__(initialamt,accName)
    self.fee = 5 # fee to withdraw (extra charges)

  def withDraw(self, amt):
    try:
      self.viableTransaction(amt + self.fee)
      self.balance = self.balance - (amt + self.fee)
      print("withdraw complete")
      self.getBalance()
    except BalanceException as error:
      print("Interrupted error : ", error)