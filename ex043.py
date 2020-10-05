#####
# Python By Example
# Exercise 043
# Christopher Hagan
#####

direction = input('Would you like to count upwards or downwards? ')
if direction.lower().startswith('u'):
    maxNumber = int(input('Enter the number to count up to: '))
    for i in range(1, maxNumber+1):
        print(i)
elif direction.lower().startswith('d'):
    minNumber = int(input('Enter a number under 20 to count down from 20 to: '))
    for i in range(20, minNumber, -1):
        print(i)
else:
    print('I don\'t understand')
