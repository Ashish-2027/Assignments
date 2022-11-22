class Dog:
    def __init__(self):
        print("Dog Details")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.coat = input("Enter Coat Color: ")

    def description(self):
        print("Hi my name is {} and i am {} years old".format(self.name,self.age))
    
    def get_info(self):
        print("The color of my coat is {}".format(self.coat))
    
class JackRussellTerrier(Dog):
    def __init__(self):
        Dog.__init__(self)

    def coat_type(self):
        print("I am a JackRussellTerrier")
        self.type = input("Coat Type: Enter 'S' for 'Soft Coated' And 'R' for 'Rough Coated': ")
        if 'S' in self.type :
            print("I am Soft-Coated")
        elif 'R' in self.type:
            print("I am Rough-Coated")
        else:
            print("Please enter correct input")

    def hunting(self):
        print("I hunt Fox")
        print("-----------------------")

class Bulldog(Dog):
    def __init__(self):
        Dog.__init__(self)

    def breed(self):
        self.breed = input("Breed: Enter 'S' for 'Spanish Bulldog', 'F' for 'French Bulldog',\
'C' for 'Continental Bulldog' And 'A' for 'American Bulldog': ")
        if 'S' in self.breed:
            print("I am a Spanish Bulldog")
        elif 'F' in self.breed:
            print("I am a French Bulldog")
        elif 'C' in self.breed:
            print("I am a Continental Bulldog")
        elif 'A' in self.breed:
            print("I am a American Bulldog")
        else:
            print("Please enter correct input")
            

    def origin(self):
        print('I am originally from United Kingdom, England')

d1=JackRussellTerrier()
d1.description()
d1.get_info()
d1.coat_type()
d1.hunting()

d2=Bulldog()
d2.description()
d2.get_info()
d2.breed()
d2.origin()