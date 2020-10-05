#####
# Python By Example
# Exercise 093
# Christopher Hagan
#####

from array import *

nums = array('i', [])
removedNums = array('i', [])
while len(nums) < 5:
    newNum = int(input('Enter a number to append to the array: '))
    nums.append(newNum)

nums = sorted(nums)
print(nums)

userChoice = int(input('Enter a number to move to the new array: '))
nums.remove(userChoice)
removedNums.append(userChoice)

print(nums)
print(removedNums)
