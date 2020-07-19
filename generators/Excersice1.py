# genearate the squares of the numbers


def generate_sqr(rangeNum):
    for number in range(rangeNum):
        yield number ** 2


def get_square(number):
    for numbers in generate_sqr(number):
        print(numbers)


get_square(10)
