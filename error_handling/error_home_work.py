# handling exceptions and errors

# example 1
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Cannot be multiplied by alphabets")
finally:
    print("I am exiting")

# example 2

X = 5
Y = 0

try:
    Z = X / Y
except ZeroDivisionError:
    print("Division by zero cannot be done")
finally:
    print("I am done")

# example 3
# take user input and manupilate if they are valid

while True:
    try:
        NUMBER = int(input("Enter the number to be squared"))
    except ValueError:
        print("Not a number")
        continue
    else:
        SQUARE = pow(NUMBER, 2)
        print("Square of the number is : ", SQUARE)
