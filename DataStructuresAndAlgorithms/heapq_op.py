import heapq

numbers = [10, 12, 15, 17, 10, 20, 25, 26, 28, 30, 35, 45]

print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))

profolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(1, profolio, key=
lambda s: s['price']))

print(heapq.nsmallest(1, profolio, key=
lambda s: s['price']))

