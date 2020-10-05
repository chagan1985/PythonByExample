#####
# Python By Example
# Exercise 115
# Christopher Hagan
#####

import csv

columnHeaders = ['Book', 'Author', 'Year Released']

with open('Books.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile, fieldnames=columnHeaders)

    count = 0
    for row in reader:
        if columnHeaders[2] not in row[columnHeaders[2]]:
            print('{} - {} by {} published in {}'.format(count, row['Book'], row['Author'], row['Year Released']))
        count += 1
