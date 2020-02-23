
a = 0

while a < 10:
    print(a)
    a += 1

a, b = 0, 1

# this is a example of fibonacci sequence
while a < 90:
    print(a)
    # adding the variable as per precedence
    # 1 a = 1, b = 1
    # 2 a = 1, b = 2
    # 3 a = 2, b = 3
    # 4 a = 3, b = 5
    a, b = b, a+b

# get the number from the user in the integer format
print('')

# while condition with if and else conditions
# the number is taken from the end user
while input(" Do you want to proceed further : (Y/N) ") == 'Y':
    number = int(input(" Enter the number : "))
    # the basis if else loops
    if number == 42:
        print(" The number is the same as 42")
    elif number < 42:
        print(" The number is less than 42")
    elif number > 42:
        print(" The number is greater than 42")
    else:
        print(" The number is unknown")


words = [' This is ', ' Nothing ', ' But a sequence of characters ', ' to be printed ']

for w in words:
    print(w, len(w))


# printing the range of numbers
for i in range(5):
    print(i)

# another way of using ranges
rangeWords = [" Another set for testing", " using Range ", " this can be tested ", " more and more ", " with the ",
              "same set"]

for i in range(len(rangeWords)):
    print(rangeWords[i] + ' Word Range, indices ', i)

print(range(0, 1))

# break and continue are supported as other languages

# continue clause
for num in range(1, 10):
    if num % 2 == 0:
        print(" The number is even ", num)
        continue
    else:
        print(" The number is odd ", num)
















