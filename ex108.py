#####
# Python By Example
# Exercise 108
# Christopher Hagan
#####

file = open('Names.txt', 'a')
anotherName = input('Enter another name to add to the file: ')
file.write('{}\n'.format(anotherName))
file.close()

fileContents = open('Names.txt', 'r')
print('The contents of the file are as follows: \n\n{}'.format(fileContents.read()))
