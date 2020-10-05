#####
# Python By Example
# Exercise 091
# Christopher Hagan
#####

from array import *

nums = array('i', [15, 18, 58, 94, 58])
print(nums)
userChoice = int(input('Enter a number to query: '))

# count = 0
# for i in nums:
#     if i == userChoice:
#         count += 1

print('The number you queried exists {} time(s) in the list.'.format(nums.count(userChoice)))
