#####
# Python By Example
# Exercise 044
# Christopher Hagan
#####

number = int(input('How many people would you like to invite to your party? '))
if number < 10:
    for i in range(0, number):
        guest = input('Enter the name of your next guest: ')
        print('{} has been invited.'.format(guest))
else:
    print('Too many people!')
