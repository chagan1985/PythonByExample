#####
# Python By Example
# Exercise 145
# Christopher Hagan
#####

codeString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

def displayMenu():
    print("""\nMain Menu\n==========
1) Make a code
2) Decode a message
3) Quit\n""")
    choice = input('Enter your selection : ')
    return choice


def userEntry(operationText):
    print('\n{}\n-------------'.format(operationText))
    message = input('Please enter the message you would like to {} : '.format(operationText))
    offset = input('Now please enter the string offset you would like to apply : ')
    return message, offset


def displayMessage(message):
    print('\n\n*******\nYour message is - {}\n*******\n'.format(message))


def encryptText():
    message, offset = userEntry('Encrypt')

    result = ''
    for char in message:
        codedValue = None
        for encryptValue in range(0, len(codeString)):
            if char == codeString[encryptValue]:
                codedValue = encryptValue + int(offset)
                break
        codedValue = codedValue % len(codeString)
        result += codeString[codedValue]

    displayMessage(result)
                

def decryptText():
    message, offset = userEntry('Decrypt')

    result = ''
    for char in message:
        codedValue = None
        for encryptValue in range(0, len(codeString)):
            if char == codeString[encryptValue]:
                codedValue = encryptValue - int(offset)
                break
        codedValue = codedValue % len(codeString)
        result += codeString[codedValue]

    displayMessage(result)


userSelection = '0'
while (userSelection != '3'):
    userSelection = displayMenu()
    if userSelection in ['1', '2', '3']:
        if userSelection == '1':
            encryptText()
        elif userSelection == '2':
            decryptText()
            
    else:
        print('\n***\nInvalid selection, please try again...\n***\n')
    
print('\n\n*****\nQuitting program at user request\n*****\n\n')
