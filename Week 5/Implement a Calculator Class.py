# Python Class Calculator that performs addition, subtraction, 
# multiplication, and division of Two Numbers.

class Calculator:
    def __init__(self,num1,num2):
        self.no1 = num1
        self.no2 = num2
        print('The Two Numbers are {} and {} '.format(self.no1,self.no2))

    def addition(self):
        print('The Addition of Two Numbers is ',self.no1 + self.no2)

    def subraction(self):
        print('The Subraction of Two Numbers is ',self.no1 - self.no2)

    def multiplication(self):
        print('The Multiplication of Two Numbers is ',self.no1 * self.no2)

    def division(self):
        print('The Division of Two Numbers is ',(self.no1 / self.no2))


o1 = Calculator(20,6.5)
o1.addition()
o1.subraction()
o1.multiplication()
o1.division()