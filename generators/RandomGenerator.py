# create a generator and return random numbers between numbers
import random


def random_number(low, high, n):
    for numbers in range(n):
        yield random.randint(low, high)


def print_random_numbers(low, high, number_steps):
    # generators use the next pointer in the loop holding on to the prev value
    for numbers in random_number(low, high, number_steps):
        print(numbers)


print_random_numbers(1, 10, 12)

# iterator function example

hello_world = "Hello World"

hello_world_itr = iter(hello_world)

print(next(hello_world_itr))
