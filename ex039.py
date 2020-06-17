#####
# Python By Example
# Exercise 039
# Christopher Hagan
#####

number = int(input('Which times tables should be shown: '))
for i in range(1, 13):
    print('{} times {} = {}'.format(number, i, (i*number)))
