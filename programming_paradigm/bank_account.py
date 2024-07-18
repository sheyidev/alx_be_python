## Objective: Understand the fundamentals of OOP in 
## Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    def deposit(self, amount):
        account_balance = amount + self.account_balance
        #return account_balance
    def withdraw(self, amount):
        if account_balance > amount:
            account_balance = amount - self.account_balance
            return True
        else:
            print("You cannot alter your account balance")
            #return False

      
    def display_balance(self):
        print(f"Your current account balance is {self.account_balance}")