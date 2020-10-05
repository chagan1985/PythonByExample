#####
# Python By Example
# Exercise 090
# Christopher Hagan
#####

from array import *

nums = array('i', [])
while len(nums) < 5:
    newNum = int(input('Enter a number between 10 and 20: '))
    if (newNum >= 10) and (newNum <= 20):
        nums.append(newNum)
    else:
        print('Outside the range!')

print('Thank you!')
for i in nums:
    print(i)
