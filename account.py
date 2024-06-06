class Account:
    
    def __init__(self,):
        
        self.balance = 0
    
        print("starting balance: ", self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New balnce: ", self.balance)
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Balance: ", self.balance)
        
