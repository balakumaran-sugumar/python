#  generators can add a sequence of value over time
#  the main keyword is yield
#  can automatically suspend and resume generation

#  for example if we need 1000 variable, either we can create a list of 1000 variable or
#  wait for the function to return the value last stored and add the step size


def yeild_cube(numbers):
    for number in range(numbers):
        yield number ** 3


# print(yield_cube(10)) this will only print the address of the cube


print(list(yeild_cube(10)))


# example of a fibonacci series

def finoc(num):
    a = 1
    b = 1
    # if it a normal function than I need to store it in a variable
    # output = []
    for i in range(num):
        # if normal function output[i] = a
        yield a
        a, b = b, a + b
    # if normal function
    # using yield is more like streaming than storing the result in a output array
    # return output


#  more on the generator next function
def generator_samp(nums):
    for num in range(nums):
        yield num


def generator_loop():
    for num in generator_samp(10):
        print(str(num))


generator_loop()

generator_next = generator_samp(2)
# this will print the type of the object
print(generator_next)
# this will get the next available value in the generator
print(next(generator_next))
print(next(generator_next))

print(list(finoc(10)))
