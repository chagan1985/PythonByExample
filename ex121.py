#####
# Python By Example
# Exercise 121
# Christopher Hagan
#####

import sys
breakBetweenLines = '-------'


def addName(listOfNames):
    print(breakBetweenLines)
    name = input('Please enter a name to add to the list: ')
    print(breakBetweenLines)
    listOfNames.append(name)
    print('{} has been added to the list of names...'.format(name))


def changeName(listOfNames):
    print(breakBetweenLines)
    nameToChange = input('Please enter a name on the list you would like to change: ')
    newName = input('Please enter the name you would like to replace {} on the list: '.format(nameToChange))
    i = 0
    found = False
    while (i < len(listOfNames)) and not found:
        if nameToChange.lower() == listOfNames[i].lower():
            listOfNames[i] = newName
            print('{} has been added to the list of names and {} removed...'.format(newName, nameToChange))
            found = True
        else:
            i += 1

    if not found:
        print('{} does not exist in the list.'.format(nameToChange))


def deleteName(listOfNames):
    print(breakBetweenLines)
    nameToDelete = input('Please enter the name to delete from the list: ')
    if nameToDelete in listOfNames:
        listOfNames.remove(nameToDelete)
        print('{} has been removed from the list of names...'.format(nameToDelete))
    else:
        print('{} does not exist in the list.'.format(nameToDelete))


def listNames(listOfNames):
    print(breakBetweenLines)
    print('Current names in the list')
    print(breakBetweenLines)
    for name in listOfNames:
        print(name)


def main():
    listOfNames = []
    while True:
        print(breakBetweenLines)
        print('1) Add name to the list')
        print('2) Change a name in the list')
        print('3) Delete a name from the list')
        print('4) View the list of names')
        print('5) Quit')
        print(breakBetweenLines)
        optionSelected = input('Which operation would you like to perform: ')
        if optionSelected == '1':
            addName(listOfNames)
        elif optionSelected == '2':
            changeName(listOfNames)
        elif optionSelected == '3':
            deleteName(listOfNames)
        elif optionSelected == '4':
            listNames(listOfNames)
        elif optionSelected == '5':
            sys.exit(0)
        else:
            print(breakBetweenLines)
            print('Invalid operation selected, please try again!')


main()
