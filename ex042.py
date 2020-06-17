#####
# Python By Example
# Exercise 042
# Christopher Hagan
#####

total = 0
for i in range(0, 5):
    num = int(input('Please enter a number: '))
    addToTotal = input('Should this be added to the total? ')
    if addToTotal.lower().startswith('y'):
        total += num

print('The total is {}'.format(total))
