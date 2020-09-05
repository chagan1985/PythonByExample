#####
# Python By Example
# Exercise 138
# Christopher Hagan
#####

from tkinter import *
availableImageNumbers = ['7', '10', '18', '25', '30', '58']


def loadImage():
    if numberEntry.get() in availableImageNumbers:
        playerPhoto = PhotoImage(file = '{}.gif'.format(numberEntry.get()))
    else:
        playerPhoto = PhotoImage(file = 'cross.gif')

    playerImage.image = playerPhoto
    playerImage['image'] = playerPhoto
    playerImage.update()


window = Tk()
window.geometry('500x500')
window.title('Gif by number')

numberLabel = Label(text='Please enter a number : ')
numberLabel.place(x=100, y=50, width=175, height=25)

numberEntry = Entry(text='')
numberEntry.place(x=300, y=50, width=100, height=25)

loadButton = Button(text='Load Image', command=loadImage)
loadButton.place(x=100, y=100, width=300, height=25)

playerImage = Label(image='')
playerImage.place(x=100, y=150, width=300, height=250)

window.mainloop()
