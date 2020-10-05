#####
# Python By Example
# Exercise 022
# Christopher Hagan
#####

firstName = input('Please enter your first name in lower case: ')
surname = input('Now enter your surname, also in lower case: ')
fullName = firstName.title() + ' ' + surname.title()
print('Using Python\'s title formatter and concatenating your name leads to {}'.format(fullName))
