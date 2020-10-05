#####
# Python By Example
# Exercise 082
# Christopher Hagan
#####

firstLine = 'Baby on board, something, something Bert Ward!'
print(firstLine)
startPoint = int(input('Enter the starting point for the snippet: '))
endPoint = int(input('Enter the ending point for the snippet: '))
print('Snippet: {}'.format(firstLine[startPoint:endPoint]))
