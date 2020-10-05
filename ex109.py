#####
# Python By Example
# Exercise 109
# Christopher Hagan
#####

fileName = 'Subject.txt'

print("""Choose an operation:
1) Create a new file
2) Display the file
3) Add a new item to an existing file""")

operation = 0
while operation not in (1, 2, 3):
    operation = int(input('Make a selection 1, 2 or 3: '))
    if operation not in (1, 2, 3):
        print('Invalid selection, please try again!')

if operation == 1:
    subject = input('Please enter a school subject: ')
    file = open(fileName, 'w')
    file.write('{}\n'.format(subject))
if operation == 2:
    file = open(fileName, 'r')
    print('The contents of the file {} are: \n\n{}'.format(fileName, file.read()))
if operation == 3:
    newSubject = input('Please enter a new subject: ')
    file = open(fileName, 'a')
    file.write('{}\n'.format(newSubject))
    file.close()
    file = open(fileName, 'r')
    print('The contents of the file {} are: \n\n{}'.format(fileName, file.read()))

file.close()
