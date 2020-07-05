#####
# Python By Example
# Exercise 102
# Christopher Hagan
#####

import sys

shoeDictionary = {}
for i in range(0, 4):
    name = input('Enter the name of a person: ')
    age = int(input('Enter {}\'s age: '.format(name)))
    shoeSize = input('And shoe size: ')
    shoeDictionary[name] = {'age': age, 'shoeSize: ': shoeSize}

displayName = input('Which user details would you like to view: ')

try:
    print(shoeDictionary[displayName])
except:
    sys.exit('This person does not exist!')
