#####
# Python By Example
# Exercise 076
# Christopher Hagan
#####

attendees = []
for i in range(0, 3):
    attendees.append(input('Enter the name of someone to invite to a party: '))

addAnother = 'y'
while addAnother.lower().startswith('y'):
    addAnother = input('Would you like to add another guest: ')
    if addAnother.startswith('y'):
        attendees.append(input('Enter the name of another guest to invite to the party: '))

print('You have invited {} people to your party!'.format(len(attendees)))
