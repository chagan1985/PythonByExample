#####
# Python By Example
# Exercise 026
# Christopher Hagan
#####

word = input('Enter any word and I will convert it to \'Pig Latin\': ')
if word.lower().startswith(('a', 'e', 'i', 'o', 'u')):
    pigLatinWord = word.lower() + 'way'
else:
    pigLatinWord = word[1:len(word)].lower() + word[0].lower() + 'ay'

print('{} in \'Pig Latin\' is {}.'.format(word, pigLatinWord))
