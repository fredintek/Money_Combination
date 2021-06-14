# QUESTION
"""
Write a Python program to check the validity of a password (input from users).

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 12 characters.
"""

# CODE
import re
password = input("Input your password\n-->") #getting input from user
x = True #set a true condition for the while loop that will be changed later on to break the while loop
while x:  
    if (len(password) < 6 or len(password) > 12): #make sure characters of the password is between 6 - 12
        print('Hey password must be between 6 to 12 characters long!!')
        break
    elif not re.search("[a-z]",password): #check for lowercase letters in the password
        print('Lowercase letters should be included!')
        break
    elif not re.search("[0-9]",password): #check for Digits in the password
        print('Digits should be included!')
        break
    elif not re.search("[A-Z]",password): #check for uppercase letters in the password
        print('Uppercase letters should be included!')
        break
    elif not re.search("[$#@]",password): #check for special characters in the password
        print('Special characters such as ($, #, @) should be included!')
        break
    elif re.search("\s",password):  #getting rid of whitespaces in the password
        print('Do not include whitespaces!')
        break
    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")
    print('Try again 😁')





