# File 1 - 4.1 - 4.3

## Maximum
def maximum(value1, value2, value3):
    maxNum = value1
    if value2 > maxNum:
        maxNum = value2
    if value3 > maxNum:
        maxNum = value3
    return maxNum

print(f'The max is {maximum(12, 27, 36)}')
max(12, 27, 36)

## Minimum for three values
def minimum1(value1, value2, value3):
    minNum = value1
    if value2 < minNum:
        minNum = value2
    if value3 < minNum:
        minNum = value3
    return minNum

print(f'The min is {minimum1(12, 27, 36)}')
min(12, 27, 36)

# Minimum for an unknown number of arguments
def minimum2(*args):
    minValue = None
    for a in args:
        if minValue is None or a < minValue:
            minValue = a
    return minValue

print(f'The min is {minimum2(15, 9, 27, 14)}')
min(15, 9, 27, 14)