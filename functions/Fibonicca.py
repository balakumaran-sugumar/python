# defining a function with arguments
# this is a fibonacci series: the result is sum of the two prev numbers


def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = a+b, a
    return result


fib200 = fib(2000)
print(fib200)



