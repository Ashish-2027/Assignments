# Python function to sum all the numbers in a list.

# creating a list
list1 = [int(input('Enter list of numbers: ')).split()]

def addition_of_list(a= list()): #defining function to add values of the list
    total = 0
    for numbers in range(0,len(a)):
        total = total + a(numbers)
        return total


# printing total value
print("Sum of all elements in given list: ", addition_of_list(list1))
