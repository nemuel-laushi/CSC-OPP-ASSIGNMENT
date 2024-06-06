class Account:
    def __init__(self, account_name, account_holder):
        self.balance = 0
        self.account_number = account_number
        self.account_holder = account_holder
        print("starting balance: ", self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New balnce: ", self.balance)
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Balance: ", self.balance)
        
