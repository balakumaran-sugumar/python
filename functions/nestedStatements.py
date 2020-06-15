# nested statement and scope

# LEGB - Local, enclosing local global and built it

# here x is a local expression
lambda x: x ** 2

# enclosing function locals
# this is in global scope
name = "This is Global scope"


def print_name():
    name = "tech kumaran"

    def print_sub_func():
        # for this function name has the scope of print_name
        print("within the scope of print name : ", name)

    print_sub_func()


print_name()


# to use the actual global variable
def using_actual_global():
    global name
    name = "I changed this here and I am mocking the entire process"


# need to call the function for the value of the name to change
using_actual_global()
print("Lets see whats in here : ", name)





