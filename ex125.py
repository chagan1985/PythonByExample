#####
# Python By Example
# Exercise 124
# Christopher Hagan
#####

from tkinter import *
import random

def rollDice():
    roll = random.randint(1, 6)
    result['text'] = 'You got a {}'.format(roll)


window = Tk()
window.Geometry = ("300x200")
window.title('Rolling a dice')

button = Button(text = 'Roll Dice', command = rollDice)
button.place(x=50, y=50, width=100, height=50)

result = Message(text='')
result.place(x=50, y=125, width=100, height=50)

window.mainloop()
