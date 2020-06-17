#####
# Python By Example
# Exercise 012
# Christopher Hagan
#####

firstNum = int(input('Please enter your first number: '))
secondNum = int(input('Please enter your second number: '))

if firstNum > secondNum:
    print('{}, {}'.format(secondNum, firstNum))
else:
    print('{}, {}'.format(firstNum, secondNum))
