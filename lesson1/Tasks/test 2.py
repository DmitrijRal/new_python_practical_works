number = int(input('Enter any number '))

maxValue = int()

while number > 0:
    rest = number % 10

    if rest > maxValue:
        maxValue = rest

    number //= 10

print('Max value is:', maxValue)