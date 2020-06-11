

# the zip functionality

tup1 = (1, 2, 3, 4, 5)
tup2 = ('a', 'b', 'c', 'd', 'e')
tup3 = ('num1', 'num2', 'num3', 'num4', 'num5')

tupZipped = zip(tup1, tup2, tup3)

print(tupZipped)

# iterate over the tups

for tupList in tupZipped:
    print(tupList)

