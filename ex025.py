#####
# Python By Example
# Exercise 025
# Christopher Hagan
#####

firstName = input('Please enter your first name: ')
if len(firstName) < 5:
    surname = input('And your surname: ')
    fullName = firstName + surname
    print('Your name in upper case is {}'.format(fullName.upper()))
else:
    print('Your name in lower case is {}'.format(firstName.lower()))
