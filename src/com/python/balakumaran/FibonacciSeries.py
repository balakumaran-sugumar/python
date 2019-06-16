# assigning the variables
# code demonstrates multiple assignments and assignments
# end can be used for avoiding new line characters
a, b = 0, 1

while a < 10:
    print(a, end=',')
    a, b = b, a+b
