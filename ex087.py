#####
# Python By Example
# Exercise 087
# Christopher Hagan
#####

word = input('Enter a word: ')
for i in range(len(word), 0, -1):
    print(word[i-1])
