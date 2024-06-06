from account import Account



class bingham_savings_acc(Account):

    def __init__(self):
        super().__init__()
        self.interest_rate = 0.005

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        if amount > self.balance:
            print('ACCOUNT BALANCE IS TOO LOW')

        
        elif amount <= 700000 :
             print('access granted for withdrawal')
             print('your current balance is, '  + str(self.balance))
             

        else:
            print('amount is beyond limits')
           

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance += self.interest_rate
        print('your current balance is, '  + str(self.balance))
        
print('ONLY INPUT NUMERIC VALUES FOR AMOUNT ')

k = bingham_savings_acc()
opt = input('IF YOU WANT TO DEPOSIT INPUT a lower case"d", AND IF YOU WANT TO WITHDRAW INPUT a lower case "w": ')

if opt == 'w': 
    try:
        amw = float(input('Enter desired  withdrawal amount: '))
        k.withdrawal(amw)
    except:
        print('AMOUNT MUST BE NUMERIC')
    
if opt == 'd':
    try:
        amd = float(input('Enter deposit amount: '))
        k.deposit(amd)
    except:
        print('AMOUNT MUST BE NUMERIC')




