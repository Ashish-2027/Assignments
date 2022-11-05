# Python program to triple all numbers of a given list of integers using Python map.

# Taking input from the user and storing it in a list
nos_list = list(map(int,input('Enter a list of Numbers: ').split()))

# Tripling the values of the list 
print(list(map(lambda x:x*3, nos_list)))