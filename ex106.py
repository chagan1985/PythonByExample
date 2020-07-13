#####
# Python By Example
# Exercise 106
# Christopher Hagan
#####

file = open('Names.txt', 'w')
for name in ('Chris', 'Hannah', 'Lochlann', 'Rex', 'Emmet'):
    file.write('{}\n'.format(name))

file.close()
