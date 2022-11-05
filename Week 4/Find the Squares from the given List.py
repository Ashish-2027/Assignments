# Python program to square the elements of a list using map() function.

# Taking input from the user and storing it in a list
num_list = list(map(int,input('Enter a list of Numbers: ').split()))

# Squaring the values of the list 
print(list(map(lambda x:x**2, num_list)))