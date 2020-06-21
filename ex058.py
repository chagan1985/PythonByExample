#####
# Python By Example
# Exercise 058
# Christopher Hagan
#####

import random

correctAnswers = 0
maxQuestions = 5
for i in range(0, maxQuestions):
    firstNumber = random.randint(1, 100)
    secondNumber = random.randint(1, 100)
    userGuess = int(input('What is {} + {} : '.format(firstNumber, secondNumber)))
    if userGuess == (firstNumber + secondNumber):
        correctAnswers += 1

print('\nYou got {} correct out of {}.\n'.format(correctAnswers, maxQuestions))
