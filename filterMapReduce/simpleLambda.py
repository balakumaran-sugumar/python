def square(num):
    return pow(num, 2)


need_squared = [1, 2, 3, 4, 5, 6]

# this is function as argument
mapped_func = map(square, need_squared)

# this prints the address and nothing else
print(mapped_func)

# printing the contents of the map in for loop
for numbers in mapped_func:
    print(numbers)

# filter function, this is similar to map but filters the result based on the condition

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def even_numbers(num1):
    return num1 % 2 == 0


filteredList = filter(even_numbers, my_nums)

for num in filteredList:
    print("Even numbers are :", num)

# lambda as anonmys function
# assigning to a variable for readability
number1 = lambda number: number ** 2

print("Lambda square of 2 : ", number1(2))






