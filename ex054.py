#####
# Python By Example
# Exercise 054
# Christopher Hagan
#####

import random

coinFlip = random.choice(['Heads', 'Tails'])
userGuess = input('The computer has flipped a coin, guess whether it was heads of tails (h or t): ')
if userGuess.lower() == coinFlip[0].lower():
    print('\nYou guessed correctly!')
else:
    print('\nYour guess was wrong!')

print('\nThe result of the computer flipping a coin was {}\n'.format(coinFlip))
