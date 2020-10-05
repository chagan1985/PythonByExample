#####
# Python By Example
# Exercise 117
# Christopher Hagan
#####

import csv, random

columnHeaders = ['Name', 'Question1', 'Answer1', 'Question2', 'Answer2', 'Score']
numberOfQuestions = 2
tmp = {}
question = []
answer = []
score = 0

name = input('Enter your name: ')
tmp = {'Name': name}

for i in range(0, numberOfQuestions):
    question.append('{}{}{}'.format(random.randint(1, 10), random.choice('+-*'), random.randint(1, 30)))
    answer.append(int(input('What does {} = '.format(question[i]))))
    if (answer[i] == eval(question[i])):
        score += 1
    tmp['Question{}'.format(i+1)] = question[i]
    tmp['Answer{}'.format(i+1)] = answer[i]

tmp['Score'] = score

with open('Quiz.csv', 'a') as quizResults:
    quizFile = csv.DictWriter(quizResults, fieldnames=columnHeaders)
    quizFile.writerow(tmp)
