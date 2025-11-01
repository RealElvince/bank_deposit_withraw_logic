class BankAccount:
    def __init__(self,account_holder,account_balance):
        self.account_holder = account_holder
        self.account_balance = account_balance

    
    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Dear {self.account_holder},{amount} has been deposited into your bank account. New balance is {self.account_balance}.")
        

    def withdraw(self,amount):
        pass