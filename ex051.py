#####
# Python By Example
# Exercise 051
# Christopher Hagan
#####

greenBottles = 10
for greenBottles in range(10, 0, -1):
    print("There are {} green bottles hanging on the wall,\n"
          "{} green bottles hanging on the wall,\n"
          "and if 1 green bottle was to accidentally fall.".format(greenBottles, greenBottles))
    userGuess = 0
    while userGuess != greenBottles-1:
        userGuess = int(input('How many green bottles will be hanging on the wall? '))
        if userGuess != greenBottles-1:
            print('No, try again.')
    print('There will be {} green bottles hanging on the wall.\n\n'.format(userGuess))

print('There are no more green bottles hanging on the wall.')
