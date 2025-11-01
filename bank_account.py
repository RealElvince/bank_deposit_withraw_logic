class BankAccount:
    def __init__(self,account_holder,account_balance):
        self.account_holder = account_holder
        self.account_balance = account_balance
        self.transactions = []

    
    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            self.transactions.append(f"Amount Deposited:{amount}")
            print(f"Dear {self.account_holder},{amount} has been deposited into your bank account. New balance is {self.account_balance}.")
        

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal!")
        elif self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Dear {self.account_holder}, you have withdrawn {amount}. Your new balance is {self.account_balance}.")

        else:
            print("Insufficient Funds!")


account = BankAccount("Elijah Doe",30_000)
account.deposit(4500)
account.withdraw(10000)
account.withdraw(450000)
account.withdraw(0)