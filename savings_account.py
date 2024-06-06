from account import Account



class bingham_savings_acc(Account):

    def __init__(self, acount_n, acount_h):
        super().__init__()
        self.interest_rate = 0.005
        self.n = acount_n
        self.h = acount_h

    def withdrawal(self, amount):
        
        if amount > self.balance:
            print(h +' YOUR ACCOUNT BALANCE IS TOO LOW')

        
        elif amount <= 700000 :
             self.balance = self.balance - amount
             print('access granted for withdrawal')
             print(h +' your current balance is, '  + str(self.balance))
             

        else:
            print(h + ' amount is beyond limits')
           

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.balance += self.balance*self.interest_rate
        print(h +' your current balance is, '  + str(self.balance))
        
print('ONLY INPUT NUMERIC VALUES FOR AMOUNT ')

h = input('Enter your account user name: ')
n = input('Enter your account number: ')
k = bingham_savings_acc(n,h)
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
