#  decorators are used when you want to add more code to the existing code
#  this is when you want to use the original method instead of modifying it


#  function that takes in a argument and returns a function
# this is returning functions

def main_func(name="Bala"):
    def greet():
        return "Greeetings " + name

    def welcome():
        return "Welcome " + name

    if name == 'Bala':
        return greet
    else:
        return welcome


bala_greet = main_func()
print(bala_greet())

kumaran_welcome = main_func("Kumaran")
print(kumaran_welcome())


# This is when we have functions are arguments

def arg_functions(func_as_argument):
    return func_as_argument()


print(arg_functions(main_func()))


# example of a decorator function

def new_decorator(decorator_func):
    def inner_function():
        print("This is before the decorator")
        decorator_func()
        print("This is after the decorator")

    return inner_function


def test_decorator():
    print("This can be injected in the decorator")


# this needs to be done if the decorator is not used
# testing_decorator = new_decorator(test_decorator)


# this can be done with a simpler way
@new_decorator
def test_with_annotation():
    print("Testing decorator with annotation")


test_with_annotation()
