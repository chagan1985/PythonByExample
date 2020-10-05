#####
# Python By Example
# Exercise 099
# Christopher Hagan
#####

import sys

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(list)
userSet = int(input('Which set of values is the value you would like to view in? '))
userValue = int(input('Which value in this set would you like to view? '))

try:
    print('The value present in [{}][{}] is {}'.format(userSet, userValue, list[userSet][userValue]))
except :
    sys.exit('This value does not exist!')

updateValue = input('Would you like to update this value (yes or no): ')
if updateValue.lower().startswith('y'):
    newValue = int(input('Enter the new value to input: '))
    list[userSet][userValue] = newValue

print('The set of values present in [{}] are {}'.format(userSet, list[userSet]))
