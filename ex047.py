#####
# Python By Example
# Exercise 047
# Christopher Hagan
#####

firstNum = int(input('Enter the first number to be added together: '))
total = firstNum
addAnother = 'y'
while addAnother.lower().startswith('y'):
    additionalNum = int(input('Enter the next number to add: '))
    total += additionalNum
    addAnother = input('Would you like to add another number to the total: ')

print('The final total of these numbers is {}'.format(total))
