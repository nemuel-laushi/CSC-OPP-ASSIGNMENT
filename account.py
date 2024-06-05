class Account:
    def __init__(self):
        self.balance = 00000
        print("starting balance: ", self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("New balnce: ", self.balance)
    
    def deposit(self, amount):
        self.balance = self.balance - amount
        print("Blance: ", self.balance)
        