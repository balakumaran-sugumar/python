# creating the first class


class FirstClass:

    # this is the constructor of the class
    def __init__(self, parameter):
        self.parameter = parameter

    # this is for submodule the method
    def testing_method(self, number):
        print("This is submodule the method call ", self.parameter, number)


my_first_class = FirstClass(parameter="Test")

my_first_class.testing_method(12)
