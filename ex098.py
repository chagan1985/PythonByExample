#####
# Python By Example
# Exercise 098
# Christopher Hagan
#####

import sys

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(list)
userSet = int(input('Which set of values would you like to view? '))

try:
    print('The set of values present in [{}] are {}'.format(userSet, list[userSet]))
except :
    sys.exit('This value does not exist!')

newValue = int(input('Enter a value to add to this set: '))
list[userSet].append(newValue)
print('The set of values present in [{}] are {}'.format(userSet, list[userSet]))
