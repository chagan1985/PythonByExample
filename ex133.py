#####
# Python By Example
# Exercise 133
# Christopher Hagan
#####

from tkinter import *

def pressButton():
    name = nameEntry.get()
    helloName['text'] = 'Hello {}!'.format(name)


window = Tk()
window.geometry('500x600')
window.title('Names')
#window.wm_iconbitmap('python.ico')

logo = PhotoImage(file = 'bender1_resized.gif')
logoimage = Label(image=logo)
logoimage.place(x=150, y=50, width=200, height=200)

message = Label(text='Enter your name : ')
message.place(x=50, y=300, width=150, height=25)

nameEntry = Entry(text='')
nameEntry.place(x=250, y=300, width=200, height=25)

pressMeButton = Button(text='Press me', command=pressButton)
pressMeButton.place(x=50, y=350, width=150, height=25)

helloName = Label(text='')
helloName.place(x=250, y=350, width=200, height=25)

window.mainloop()
