#####
# Python By Example
# Exercise 120
# Christopher Hagan
#####

import random


def menu():
    validOptionSelected = False
    while not validOptionSelected:
        print('----------')
        print('1) Addition')
        print('2) Subtraction')
        print('----------')
        selection = input('Enter 1 or 2: ')
        print('----------')
        if selection in ('1', '2'):
            validOptionSelected = True
        else:
            print('Not allowed, please try again...')

    return selection


def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    userGuess = int(input('What is {} + {} = '.format(num1, num2)))
    actualAnswer = num1 + num2
    return (userGuess, actualAnswer)


def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    userGuess = int(input('What is {} - {} = '.format(num1, num2)))
    actualAnswer = num1 - num2
    return(userGuess, actualAnswer)


def checkAnswer(userGuess, actualAnswer):
    if userGuess == actualAnswer:
        print('Correct')
    else:
        print('Incorrect, the answer is {}'.format(actualAnswer))


def main():
    selection = menu()
    if selection == '1':
        userGuess, actualAnswer = addition()
    else:
        userGuess, actualAnswer = subtraction()
    checkAnswer(userGuess, actualAnswer)


main()
