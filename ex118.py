#####
# Python By Example
# Exercise 118
# Christopher Hagan
#####

def getNum():
    isNumber = False
    while not isNumber:
        enteredNumber = input('Please enter a number: ')
        try:
            num = int(enteredNumber)
            isNumber = True
        except:
            print('This is not a valid number, try again!')

    return num


def countToNum(num):
    for i in range(0, num):
        print('{}, '.format(i+1), end='')


countToNum(getNum())
