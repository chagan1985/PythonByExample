#####
# Python By Example
# Exercise 049
# Christopher Hagan
#####

compnum = 50
guess = count = 0
while guess != compnum:
    guess = int(input('Try to guess the hidden number: '))
    if guess < compnum:
        print('Your guess was too low! Please have another guess.')
    elif guess > compnum:
        print('Your guess was too high! Please have another guess.')
    count += 1

print('Well done it took you {} guesses'.format(count))
