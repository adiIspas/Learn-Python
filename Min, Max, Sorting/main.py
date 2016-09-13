numbers = {
    'A' : 10,
    'B' : 5,
    'C' : 7,
    'D' : 8,
    'E' : 9
    }

packMin = zip(numbers.values(), numbers.keys())
packMax = zip(numbers.values(), numbers.keys())
packSorted = zip(numbers.values(), numbers.keys())

print(min(packMin))
print(max(packMax))
print(sorted(packSorted))