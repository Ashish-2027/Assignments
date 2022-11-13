# Python Class Account with another Class Savings account for handling a 
# bank account using concepts of inheritance

class Account:
    def __init__(self,title = None, balance = 0):
        self.name = title
        self.bal = balance
 
    def deposit(self, amount):
        self.amt = amount
        self.bal = self.bal + self.amt
        print('Rupees {} deposited into Account'.format(self.amt))

    def withdrawal(self, amount):
        self.amt = amount
        self.bal = self.bal - self.amt
        print('Rupees {} withdrew from Account'.format(self.amt))

    def getbal(self):
        print('The Balance amount is ',self.bal)  

class SavingsAccount(Account):
    def __init__(self,title = None, balance = 0, interest_rate = 0):
        self.int_rate = interest_rate
        Account.__init__(self,title,balance)
    def display(self):
        print('{} has balance of Rupees - {} in his Account, which has a Interest Rate of {}% p.a.'.format(self.name,self.bal,self.int_rate))

    def interest_amount(self):
        print('The Interest amount for the balance of {} is {}.'.format(self.bal,(self.int_rate * self.bal)/100))

ac1 = SavingsAccount('Ashish', 5000 , 3)
ac1.display()
ac1.deposit(1000)
ac1.getbal()
ac1.withdrawal(300)
ac1.getbal()
ac1.interest_amount()