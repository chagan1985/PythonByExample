#####
# Python By Example
# Exercise 148
# Christopher Hagan
#####

import csv, os, shutil

fileName = 'userPassword.csv'
columnHeaders = ['User', 'Password']


def menuTitle(menuName):
    print('\n---\n{}\n---\n'.format(menuName))


def statusMessage(message):
    print('\n+++\n{}\n+++\n'.format(message))


def newPasswordRating():
    rating = 0
    atLeastOneCaptial = atLeastOneLower = atLeastOneNumber = atLeastOneSpecial = False
    while (rating < 3):
        newPassword = input('Enter the new password for this user: ')

        # Password should be at least 8 characters
        if len(newPassword) >= 8:
            rating += 1

        for char in newPassword:
            if not(atLeastOneCaptial) and (char.isupper()):
                rating += 1
                atLeastOneCaptial = True
            if not(atLeastOneLower) and (char.islower()):
                rating += 1
                atLeastOneLower = True
            if not(atLeastOneNumber) and (char in '0123456789'):
                rating += 1
                atLeastOneNumber = True
            if not(atLeastOneSpecial) and (char in '!£$%&'):
                rating += 1
                atLeastOneSpecial = True

        if (rating == 5):
            print('\nThis is a strong password.')
        elif (rating >= 3 and rating <= 4):
            print('\nThis password could be improved.')
        else:
            print('\nThis password is too weak, please try again...\n')
            rating = 0

    return newPassword


def addUser():
    menuTitle('Add a new User')
    newUser = input('Enter the ID of the user: ')
    newPassword = newPasswordRating()
    fileAlreadyExists = os.path.isfile(fileName)
    with open(fileName, 'a') as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames=columnHeaders)
        if not fileAlreadyExists:
            fileWriter.writeheader()
        fileWriter.writerow({'User': '{}'.format(newUser), 'Password': '{}'.format(newPassword)})

    statusMessage('User Added')


def createListOfUsers():
    userList = []
    try:
        with open(fileName, 'r') as csvFile:
            fileReader = csv.DictReader(csvFile, fieldnames=columnHeaders)

            next(fileReader)
            for row in fileReader:
                userList.append(row['User'])
    except (FileNotFoundError):
        print('File \'{}\' does not exist...'.format(fileName))
    
    return userList


def changePassword():
    menuTitle('Change a Password')
    userToUpdate = input('Which User\'s Password should be updated: ')
    if userToUpdate in createListOfUsers():
        print('Updating password for user {}...\n'.format(userToUpdate))
        newPassword = newPasswordRating()
        updatedFile = '{}_up'.format(fileName)
        with open(fileName, 'r') as originalFile, open(updatedFile, 'w') as newFile:
            fileReader = csv.DictReader(originalFile, fieldnames=columnHeaders)
            fileWriter = csv.DictWriter(newFile, fieldnames=columnHeaders)

            for row in fileReader:
                if (row['User'] == userToUpdate):
                    fileWriter.writerow({'User': '{}'.format(row['User']), 'Password': '{}'.format(newPassword)})
                else:
                    fileWriter.writerow({'User': '{}'.format(row['User']), 'Password': '{}'.format(row['Password'])})
        
        shutil.move(updatedFile, fileName)
        statusMessage('Password Updated')


def displayUsers():
    menuTitle('List of Users')
    for user in createListOfUsers():
        print(user)
    print('\n-----')


userSelection = '0'
while (userSelection != '4'):
    print("""\n===========\nPasswords\n===========
1) Create a new user ID
2) Change a password
3) Display all User IDs
4) Quit\n""")
    userSelection = input('Enter Selection: ')
    if userSelection in ['1', '2', '3', '4']:
        if userSelection == '1':
            addUser()
        elif userSelection == '2':
            changePassword()
        elif userSelection == '3':
            displayUsers()
    else:
        print('\n***\nInvalid selection\n***\n')
