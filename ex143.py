#####
# Python By Example
# Exercise 143
# Christopher Hagan
#####

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

publicationAfterYear = int(input('Enter the year after which you would like to view published books : '))

print(publicationAfterYear)

cursor.execute("SELECT * FROM Books WHERE DatePublished > {} ORDER BY DatePublished".format(publicationAfterYear))
for book in cursor.fetchall():
    print(book)
