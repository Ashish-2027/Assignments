# Python program to count the number of even and odd numbers from a series of numbers.
list_of_nos = [23,27,66,34,56,71,88,94]

even = 0
odd = 0
for x in list_of_nos:
    if x % 2 == 0 :
        even+=1
    else :
        odd+=1
print('Even Numbers in the list is ',even)
print('Odd Numbers in the list is ',odd)