#####
# Python By Example
# Exercise 066
# Christopher Hagan
#####

import turtle, random

colours = ['red', 'blue', 'purple', 'green', 'orange', 'yellow']
sideLength = 150

for i in range(0, 8):
    turtle.color(random.choice(colours))
    turtle.forward(sideLength)
    turtle.right(45)

turtle.exitonclick()
