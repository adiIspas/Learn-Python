age = 19

if age < 18:
    print('No beer for you')
else:
    print('More beer for you')

print('')

name = 'Andreea'
wantedNameOne = 'Adi'
wantedNameTwo = 'Andrea'

if name is wantedNameOne:
    print('Hey, ' + name)
elif name is wantedNameTwo:
    print('Hey, ' + name)
else:
    print('Who are you?')


print('')

foods = ['apple', 'bacon', 'bread', 'ice cream']

currentFood = 0
for food in foods:
    currentFood += 1
    print(str(currentFood) + ') ' + 'The current food is ' + (food + ' ') * currentFood)


print('')

for number in range(0,10,2):
    print("Current number is " + str(number))

print('')

value = 0
while value < 5:
    print('My value is ' + str(value))
    value += 1;