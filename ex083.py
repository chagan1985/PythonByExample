#####
# Python By Example
# Exercise 083
# Christopher Hagan
#####

repeat = True
while repeat:
    word = input('Enter a word in upper case: ')
    if word.isupper():
        repeat = False
    else:
        print('Please try again...')
