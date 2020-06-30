#####
# Python By Example
# Exercise 092
# Christopher Hagan
#####

from array import *
import random

firstArray = array('i', [])
secondArray = array('i', [])

while len(firstArray) < 3:
    newNum = int(input('Please enter a number to append on the array: '))
    firstArray.append(newNum)

for i in range(0, 5):
    secondArray.append(random.randint(0, 999))

firstArray.extend(secondArray)
firstArray = sorted(firstArray)
for i in firstArray:
    print(i)
