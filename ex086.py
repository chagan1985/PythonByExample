#####
# Python By Example
# Exercise 086
# Christopher Hagan
#####

newPass = input('Please enter a new password: ')
reenterPass = input('Please re-enter the password: ')

if newPass == reenterPass:
    print('Thank you')
elif newPass.lower() == reenterPass.lower():
    print('They must be in the same case')
else:
    print('Incorrect')
