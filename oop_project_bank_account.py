class BalanceException(Exception):
    pass

class BankAccount:

    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName

        print(f"\n Account '{self.name}' created. \nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account {self.name} only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete")    
            self.getBalance()
        except BalanceException as error:
            print(f"\nCannot perform withdraw: ")
            print(error)

    def transfer(self, amount, to_account):
        try:
            print(f"Begining Transfer from {self.name} to {to_account.name}")
            self.viableTransaction(amount)
            self.withdraw(amount)
            to_account.deposit(amount)
            print(f"Completed Transfer from {self.name} to {to_account.name}")
        except BalanceException as error:
            print(f"\nCannot transfer because of insufficient balance in {self.name}'s account")
            print(error)
        

class InterestRewardsAccount(BankAccount):

    def deposit(self, amount):
        return super().deposit(amount * 1.05)
    
class SavingsAccount(InterestRewardsAccount):

    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        return super().withdraw(amount + self.fee)        