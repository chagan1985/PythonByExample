#####
# Python By Example
# Exercise 088
# Christopher Hagan
#####

from array import *

nums = array('i', [])
for i in range(0, 5):
    newNum = int(input('Enter a number: '))
    nums.append(newNum)

nums = sorted(nums)
nums.reverse()
print(nums)
