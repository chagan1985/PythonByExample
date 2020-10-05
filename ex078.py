#####
# Python By Example
# Exercise 078
# Christopher Hagan
#####

listOfProgrammes = ['Dark', 'Mr Robot', 'Vikings', 'Curb Your Enthusiasm']

for i in range(0, len(listOfProgrammes)):
    print(listOfProgrammes[i])

newProgramme = input('Enter the name of another TV show: ')
positionValue = int(input('Which position index in the list should this show take: '))

listOfProgrammes.insert(positionValue, newProgramme)
print(listOfProgrammes)
