#####
# Python By Example
# Exercise 073
# Christopher Hagan
#####

foods = {}
for i in range(1, 5):
    favouriteFood =  input('Enter one of your favourite foods: ')
    foods[i] = favouriteFood

print(foods)
foods.pop(int(input('Which food by index should be removed: ')))
print(sorted(foods.values()))
