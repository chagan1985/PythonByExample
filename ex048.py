#####
# Python By Example
# Exercise 048
# Christopher Hagan
#####

total = 0
addAnother = 'y'
while addAnother.lower().startswith('y'):
    name = input('Enter the name of someone who you would like to invite to your party: ')
    total += 1
    print('{} has been invited to your party'.format(name))
    addAnother = input('Would you like to invite someone else: ')

print('The total number of people coming to your party is {}.'.format(total))
