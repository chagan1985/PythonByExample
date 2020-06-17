#####
# Python By Example
# Exercise 034
# Christopher Hagan
#####

shape = input("1) Square\n2) Triangle\n\nEnter a number:")
if shape == '1':
    length = int(input('Enter the length of one of the sides of the Square: '))
    print('The area of your Square is {}'.format(length**2))
elif shape =='2':
    height = int(input('Enter the height of the Triangle: '))
    breadth = int(input('Enter the breadth of the Triangle: '))
    print('The area of your Triangle is {}'.format((height * breadth) / 2))
else:
    print('Invalid option!')
