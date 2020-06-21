#####
# Python By Example
# Exercise 056
# Christopher Hagan
#####

import random

randomNumber = random.randint(1, 10)
guess = 0
while guess != randomNumber:
    guess = int(input('Guess the computer\'s random number between 1 and 10: '))

print('Correct, the computer\'s number was {}'.format(randomNumber))
