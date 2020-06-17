#####
# Python By Example
# Exercise 016
# Christopher Hagan
#####

raining = input('Is it raining? ')

if raining.lower() == 'yes':
    windy = input('Is it windy too? ')
    if windy.lower() == 'yes':
        print('It is too windy for an umbrella!')
    else:
        print('Take an umbrella!')
else:
    print('Enjoy your day!')
