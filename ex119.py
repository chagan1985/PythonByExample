#####
# Python By Example
# Exercise 119
# Christopher Hagan
#####

import random

def generateRandomNumber():
    low = int(input('Enter the lower boundary for a random number: '))
    high = int(input('Enter the higher boundary for a random number: '))
    comp_num = random.randint(low, high)
    return comp_num


def guessNumber():
    print('I am thinking of a number...')
    userGuess = int(input('What number am I thinking of: '))
    return userGuess


def main():
    correctGuess = False
    randomNumber = generateRandomNumber()
    while not correctGuess:
        guess = guessNumber()
        if randomNumber == guess:
            print('Correct, you win!')
            correctGuess = True
        else:
            if guess < randomNumber:
                print('Too Low')
            else:
                print('Too High')
            print('Guess Again!')


main()
