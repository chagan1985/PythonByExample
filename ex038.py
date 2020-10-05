#####
# Python By Example
# Exercise 038
# Christopher Hagan
#####

name = input('Please enter your name: ')
repetitions = int(input('How many times should I loop through the characters in'
                        ' your name? '))
for i in range(0, repetitions):
    print(name[i % len(name)])
