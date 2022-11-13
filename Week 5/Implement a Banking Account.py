# Python Class Account with another Class Savings account using the concepts of inheritance.

class Account:
    def __init__(self,title = None, balance = 0):
        self.name = title
        self.bal = balance

class SavingsAccount(Account):
    def __init__(self,title = None, balance = 0, interest_rate = 0):
        self.int_rate = interest_rate
        Account.__init__(self,title,balance)
    def display(self):
        print('{} has balance of Rupees - {} in his Account, which has a Interest Rate of {}% p.a.'.format(self.name,self.bal,self.int_rate))

ac1 = SavingsAccount('Ashish', 5000 , 3)
ac1.display()