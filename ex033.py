#####
# Python By Example
# Exercise 033
# Christopher Hagan
#####

numerator = int(input('Enter a whole number as the numerator: '))
denominator = int(input('Enter another whole number which will be the denominator: '))
print('{} divided by {} is {} with {} remaining.'.format(numerator, denominator, (numerator // denominator), (numerator % denominator)))
