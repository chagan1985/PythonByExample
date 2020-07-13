#####
# Python By Example
# Exercise 105
# Christopher Hagan
#####

file = open('Numbers.txt', 'w')
for i in range(5, 26, 5):
    file.write('{}, '.format(i))

file.close()
