#####
# Python By Example
# Exercise 075
# Christopher Hagan
#####

numbersList = [436, 745, 897, 603]

for i in range(0, len (numbersList)):
    print(numbersList[i])

userNumber = int(input('Enter a three digit number: '))
if userNumber in numbersList:
    print('This is the number with index {}'.format(numbersList.index(userNumber)))
else:
    print('This is not in the list.')
