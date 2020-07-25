#####
# Python By Example
# Exercise 112
# Christopher Hagan
#####

import csv

columnHeaders = ['Book', 'Author', 'Year Released']

newBook = input('Enter a new book to add: ')
newAuthor = input('Enter the Author of the book: ')
newYear = input('Enter the year the book was released: ')

newEntry = {'Book': newBook, 'Author': newAuthor, 'Year Released': newYear}

with open('Books.csv', 'a') as csvFile:
    booksFile = csv.DictWriter(csvFile, delimiter=',', fieldnames=columnHeaders)
    booksFile.writerow(newEntry)

with open('Books.csv', 'r') as updatedCsvFile:
    reader = csv.reader(updatedCsvFile)

    for row in reader:
        print(row)
