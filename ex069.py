#####
# Python By Example
# Exercise 069
# Christopher Hagan
#####

countriesTuple = ('Iceland', 'Greenland', 'Norway', 'Finland', 'Sweden')

print('Some countries are : {}'.format(countriesTuple))
userChoice = input('Enter one of the countries: ')
print('This country has index {} in the tuple.'.format(countriesTuple.index(userChoice)))
