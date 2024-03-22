from oop_project_bank_account import *  # import all

Vandana = BankAccount(2000, "Vandana")
Sanjay = BankAccount(1000, "Sanjay")

Sanjay.getBalance()
Vandana.getBalance()

Vandana.deposit(500)

Vandana.withdraw(5000)
Vandana.withdraw(50)

Vandana.transfer(10000, Sanjay)
Vandana.transfer(100, Sanjay)

Idhant = InterestRewardsAccount(1000, "Idhant")
Idhant.getBalance()
Idhant.deposit(100)
Idhant.transfer(50, Vandana)

Khulbu = SavingsAccount(1000, "Khulbu")
Khulbu.getBalance()
Khulbu.deposit(500)
Khulbu.withdraw(200)