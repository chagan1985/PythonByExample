#####
# Python By Example
# Exercise 094
# Christopher Hagan
#####

from array import *

nums = array('i', [7, 18, 47, 58, 94])
validChoice = False

print(nums)
while not validChoice:
    userChoice = int(input('Enter a number to remove: '))
    if userChoice in nums:
        print('{} is in position {} of the array.'.format(userChoice, nums.index(userChoice)))
        validChoice = True
    else:
        print('Invalid item. Please try again!')
