# Python program to get the Fibonacci series between 0 to 50
print("Fibonacci Series")
desired_number = int(input("Enter Any Number Between 0-50 : "))

# first two numbers of the Fibonacci series
fib1 = 0
fib2 = 1

count = 0

if desired_number <= 0: #when input is a negative integer or Zero
   print("Please enter a positive integer")
elif desired_number == 1: #when input is equal to 1
   print("Fibonacci sequence upto",desired_number,":")
   print(fib1)
elif desired_number > 50: # when input is greater than 50
    print("Wrong Input, Please enter Number from 0-50")
else:
   print("Fibonacci sequence for",desired_number,":")
   while count < desired_number:
       print(fib1,end = " ")
       num1 = fib1 + fib2
       fib1 = fib2
       fib2 = num1
       count += 1