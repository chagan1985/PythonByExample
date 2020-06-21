#####
# Python By Example
# Exercise 045
# Christopher Hagan
#####

total = 0
while total < 50:
    num = int(input('Enter a number to add to the total: '))
    total += num
    print('The total is now {}'.format(total))
