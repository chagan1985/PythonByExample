#####
# Python By Example
# Exercise 068
# Christopher Hagan
#####

import turtle, random

# Meh I don't want to wait all day....
randomShape = random.randint(4, 12)
# Division by zero is bad m'kay!
randomLines = random.randint(1, 20)
# Allow 50...200 in levels of 10
shapeSide = random.randrange(50, 200, 10)

for i in range(0, randomLines):
    turtle.left(int(360/randomLines))
    for j in range(0, randomShape):
        turtle.forward(shapeSide)
        turtle.left(int(360 / randomShape))

turtle.exitonclick()
