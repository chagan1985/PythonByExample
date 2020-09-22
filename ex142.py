#####
# Python By Example
# Exercise 142
# Christopher Hagan
#####

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT * FROM Authors;""")
for author in cursor.fetchall():
    print(author)

authorBirthPlace = input('Enter the place of birth of the author(s) you would like to search : ')

cursor.execute("SELECT * FROM Books WHERE Author IN (SELECT Name FROM Authors WHERE PlaceOfBirth='{}');".format(authorBirthPlace))
for x in cursor.fetchall():
    print(x)
