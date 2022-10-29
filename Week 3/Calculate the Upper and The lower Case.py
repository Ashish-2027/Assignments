# Python function that accepts a string and calculate the number of upper case letters 
# and lower case letters.

def count_upper_lower(letters): #function to calculate uppercase and lowercase letters
    lowercase_count = 0
    uppercase_count = 0

    for letter in letters:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower(): 
            lowercase_count += 1
        else:
            pass

    print ('The Number of Upper case letters are :', uppercase_count)
    print ('The Number of Lower case letters are :', lowercase_count)

count_upper_lower(input('Please enter your sentence: ')) #taking input from thed user
# The above code ignores integer values.