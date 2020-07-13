#####
# Python By Example
# Exercise 107
# Christopher Hagan
#####

fileName = 'Names.txt'
file = open(fileName, 'r')

print('The contents of the file "{}" can be seen below :\n\n{}'.format(fileName, file.read()))
file.close()
