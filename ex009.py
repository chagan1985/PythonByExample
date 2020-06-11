#####
# Python By Example
# Exercise 009
# Christopher Hagan
#####

numberOfDays = int(input('Enter the number of days to convert into hours, minutes and seconds: '))
print('{} days = {} hours = {} minutes = {} seconds'.format(numberOfDays, (numberOfDays * 24), (numberOfDays * 1440), (numberOfDays * 86400)))
