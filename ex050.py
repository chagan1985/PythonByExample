#####
# Python By Example
# Exercise 050
# Christopher Hagan
#####

num = 0
while num < 10 or num > 20:
    num = int(input('Please enter a number between 10 and 20: '))
    if num < 10:
        print('Too low, please try again!')
    elif num > 20:
        print('Too high, please try again!')

print('Thank you!')
