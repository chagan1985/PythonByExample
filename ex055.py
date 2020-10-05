#####
# Python By Example
# Exercise 055
# Christopher Hagan
#####

import random

randomNumber = random.randint(1, 5)
userGuess = int(input('Guess the random number between 1 and 5: '))
if userGuess == randomNumber:
    print('Well done!')
else:
    if userGuess < randomNumber:
        print('Too low!')
    else:
        print('Too High!')
    userGuess = int(input('Guess again: '))
    if userGuess == randomNumber:
        print('Correct!')
    else:
        print('You lose!')
