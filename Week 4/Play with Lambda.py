# Python program to create a lambda function that adds 25 to a given number passed in as an argument.

input_no = int(input('Enter Your Number: ')) # Taking input from the user

adding_25 = lambda x : x + 25 # Lambda funtion for adding 25 to the input

print(adding_25(input_no)) 