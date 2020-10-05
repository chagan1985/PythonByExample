#####
# Python By Example
# Exercise 041
# Christopher Hagan
#####

name = input('Please enter your name: ')
repetitions = int(input('How many times should I repeat your name: '))
if repetitions < 10:
    textToRepeat = name
else:
    textToRepeat = 'Too high'
    repetitions = 3

for i in range(0, repetitions):
    print(textToRepeat)
