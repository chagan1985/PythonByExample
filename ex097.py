#####
# Python By Example
# Exercise 097
# Christopher Hagan
#####

list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

print(list)
userSet = int(input('Which set of values is the value you would like to view in? '))
userValue = int(input('Which item in this should be shown individually? '))

try:
    print('The value present in [{}][{}] is {}'.format(userSet, userValue, list[userSet][userValue]))
except :
    print('This value does not exist!')
