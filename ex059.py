#####
# Python By Example
# Exercise 059
# Christopher Hagan
#####

import random

colours = ['Red', 'Blue', 'Green', 'Purple', 'Orange']
computersColour = random.choice(colours)
userGuess = input('Guess the colour the computer choose between {} :'.format(colours))
while userGuess.lower() != computersColour.lower():
    print('\nGuess again!\n')
    if computersColour == 'Red':
        print('You must be RED with anger!')
    elif computersColour == 'Green':
        print('You must be GREEN with envy!')
    elif computersColour == 'Blue':
        print('You are probably feeling BLUE right now!')
    elif computersColour == 'Purple':
        print('You are probably PURPLE with indifference!')
    elif computersColour == 'Orange':
        print('Wooo go BRONCOS!!!')

    userGuess = input('Guess again: ')

print('\nWell done! The computer\'s colour was {}'.format(computersColour))
