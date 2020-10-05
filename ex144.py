#####
# Python By Example
# Exercise 144
# Christopher Hagan
#####

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

authorName = input('Enter the name of the author you would like to search for : ')

cursor.execute("SELECT * FROM Books WHERE Author = '{}'".format(authorName))
file = open('BookInfoQuery.txt', 'w')
for book in cursor.fetchall():
    file.write('{} - {} - {} - {}\n'.format(book[0], book[1], book[2], book[3]))

file.close()
db.close()
