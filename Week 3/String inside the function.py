# Python program to reverse a string using a user defined function.

input_word = input('Please enter your string : ') # taking input from the user


def mirror(s): #function to reverse the string
    word = ""
    for i in s:
        word = i + word
    return word

print("The reversed string is : ", mirror(input_word))