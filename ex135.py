#####
# Python By Example
# Exercise 135
# Christopher Hagan
#####

from tkinter import *

def clickMe():
    window['bg'] = colourBox.get()

window = Tk()
window.geometry('500x500')
window.title('Select Colour')

colourBox = StringVar(window)
colourBox.set('Select Colour')
colourList = OptionMenu(window, colourBox, 'Blue', 'Green', 'Orange', 'Purple')
colourList.place(x=100, y=50, width=300, height=25)

clickMeButton = Button(text='Click Me', command=clickMe)
clickMeButton.place(x=100, y=200, width=300, height=25)

window.mainloop()
