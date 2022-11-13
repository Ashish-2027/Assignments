# Python Class Point which squares the values and returns their sum.

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sq1 = self.x * self.x
        sq2 = self.y * self.y
        sq3 = self.z * self.z
        print('The Sum of the Squares of {} , {} and {} is '\
            .format(self.x,self.y,self.z), sq1+sq2+sq3)

v1 = Point(7,8,4)
v1.sqSum()