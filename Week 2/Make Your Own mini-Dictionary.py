# Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

ascii_dict = {}
char = input('Enter a uppercase or lowercase character : ')

if (char.islower() == False) and (char.isupper() == False): # If both the conditions are not True.
    print('Please Enter only one character')
    pass

else: 
    for i in range(97,123):  # If the entered character is Lowercase
        if char.islower() == True:
            ascii_dict[chr(i)] = i


    for z in range(65,91) : # If the entered character is Uppercase
        if char.isupper() == True:
            ascii_dict[chr(z)] = z
    
    print('ASCII Values', ascii_dict)
