name, date, price = ["Laptop", "September 15", 3000]

print(name,date,price)

def drop(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)

    print(avg)

drop([1,2,3,4,5])

first = ['A','B','C']
last = ['X', 'Y', 'Z']

letters = zip(first,last)

for a, b in letters:
    print(a, '-', b)