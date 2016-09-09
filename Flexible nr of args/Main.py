def total(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

print(total(2))
print(total(10,12))
print(total(10,12,3))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(total(*numbers))