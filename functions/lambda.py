
# small anonymous functions can be created using Lambda function


def make_increament(n):
    return lambda x: x + n


f = make_increament(42)

print(f(0))

print(f(1))

print(f(2))


# another example of usage of lambda

pair = [(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')]

pair.sort(key=lambda pairs: pairs[1])

print(pair)
