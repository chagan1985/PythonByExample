#####
# Python By Example
# Exercise 089
# Christopher Hagan
#####

from array import *
import random

nums = array('i', [])
for i in range(0, 5):
    nums.append(random.randint(0, 999))

for i in nums:
    print(i)
