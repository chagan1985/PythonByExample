#####
# Python By Example
# Exercise 070
# Christopher Hagan
#####

countriesTuple = ('Iceland', 'Greenland', 'Norway', 'Finland', 'Sweden')

print('Some countries are : {}'.format(countriesTuple))
userChoice = int(input('Enter the index of a country: '))
print('This index is for the country {} in the tuple.'.format(countriesTuple[userChoice]))
