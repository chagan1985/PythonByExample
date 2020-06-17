#####
# Python By Example
# Exercise 021
# Christopher Hagan
#####

firstName = input('What is your first name? ')
surname = input('What is your surname? ')
fullName = firstName + ' ' + surname
print('You full name is {}, which is {} characters long.'.format(fullName, (len(firstName) + len(surname))))
