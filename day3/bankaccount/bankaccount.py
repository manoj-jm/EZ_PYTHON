from day3.bankaccount.oops import *

Dave = BankAccount(1000,"Dave")
manoj = BankAccount(30000,"manoj")
vishwa = BankAccount(40100,"vishwa")
# vishwa.deposite(900)
# vishwa.withDraw(900)
# Dave.transferAmt(900,manoj)

manoj = InterestRewardAcct(1000, 'manoj')
# manoj.getBalance()
# manoj.deposite(100)


manoj = SavingAcct(3000, 'manoj')
manoj.withDraw(200)
