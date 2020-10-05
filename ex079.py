#####
# Python By Example
# Exercise 079
# Christopher Hagan
#####

nums = []
count = 0
while count < 3:
    nums.append(int(input('Enter a number: ')))
    print(nums)
    count += 1

wantLastNumber = input('Do you still want the last number? ')
if wantLastNumber.lower().startswith('n'):
    nums.remove(nums[-1])

print(nums)
