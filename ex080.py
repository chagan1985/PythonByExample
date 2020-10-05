#####
# Python By Example
# Exercise 080
# Christopher Hagan
#####

firstName = input('Enter your first name: ')
print('The length of your first name is {}.'.format(len(firstName)))
surname = input('Enter your surname: ')
print('The length of your surname is {}'.format(len(surname)))
fullName = '{} {}'.format(firstName, surname)
print('That would mean your full name is: {}'.format(fullName))
print('The length of your full name, including the space is {} characters.'.format(len(fullName)))
