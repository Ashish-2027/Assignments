# Python Class Student that stores two private variables Rollno & Name which 
# are modified using Getter & Setter methods

class Student:
    def __init__(self,name = 'Brijesh', rollno = 11):
        self._name = name
        self._rollno = rollno

    def set_name(self,n1):
        self._name = n1

    def get_name(self):
        print('The Name of the Student is ',self._name)

    def set_rollno(self,r1):
        self._rollno = r1

    def get_rollno(self):
        print('His Roll Number is ',self._rollno)

s1 = Student()
s1.set_name('Ashish')
s1.get_name()
s1.set_rollno(20)
s1.get_rollno()