#####
# Python By Example
# Exercise 134
# Christopher Hagan
#####

from tkinter import *
import random

randomNumberRange = range(10,50)

def checkAnswer():
    answer = int(firstNumber['text']) + int(secondNumber['text'])
    if answer == int(userAnswerValue.get()):
        print('yes')
        answerPhoto = PhotoImage(file = 'tick.gif')
    else:
        print('no')
        answerPhoto = PhotoImage(file = 'cross.gif')
    
    answerImage.image = answerPhoto
    answerImage['image'] = answerPhoto
    answerImage.update()


def nextQuestion():
    firstNumber['text'] = random.choice(list(randomNumberRange))
    secondNumber['text'] = random.choice(list(randomNumberRange))


window = Tk()
window.geometry('500x600')
window.title('Adding game')

firstNumber = Label(text='{}'.format(random.choice(list(randomNumberRange))))
firstNumber.place(x=100, y=50, width=50, height=25)

plusSymbol = Label(text='+')
plusSymbol.place(x=200, y=50, width=50, height=25)

secondNumber = Label(text='{}'.format(random.choice(list(randomNumberRange))))
secondNumber.place(x=300, y=50, width=50, height=25)

answerLabel = Label(text='Answer : ')
answerLabel.place(x=125, y=100, width=75, height=25)

userAnswerValue = Entry(text='')
userAnswerValue.place(x=225, y=100, width=100, height=25)

checkAnswerButton = Button(text='Check Answer', command=checkAnswer)
checkAnswerButton.place(x=100, y=150, width=300, height=25)

answerImage = Label(image='')
answerImage.place(x=100, y=200, width=300, height=200)

nextQuestionButton = Button(text='Next Question', command=nextQuestion)
nextQuestionButton.place(x=100, y=450, width=300, height=50)

window.mainloop()
