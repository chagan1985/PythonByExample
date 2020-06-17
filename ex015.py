#####
# Python By Example
# Exercise 015
# Christopher Hagan
#####

colour = input('What is your favourite colour? ')

if colour.lower() == 'red':
    print('I like red too!')
else:
    print('I don\'t like {}, I prefer red.'.format(colour))
