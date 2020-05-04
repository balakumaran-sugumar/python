import math
import statistics

# from page 1 - 33 consolidated into a single file

# declaring a list
# can hold a mixture of different data types
data = ['ACME', 50, 91.1, (2020, 2, 19)]

# simple assignment
name, share, price, date = data
print("Current date : ", date)

# assigning more than one variable
name, share, price, (year, month, date) = data
print("Current year :", year)


# * expression, it makes it easy to handle large sets of data

# example here is there are 20+ subjects, you dont want to count the
# first and the last marks and average out the remaining

def avg_out_marks(grades):
    first, *middle, last = grades
    return statistics.mean(middle)


# printing out the average
grades = [1, 40, 38, 39, 40, 43, 45, 44, 48, 2]
print("Average of the middle marks : ", avg_out_marks(grades))

# example of assigning multiple phone numbers of a person
record = ['Bala', 'Computer Science', 'Python', '413-407-8334', '412-405-7756']
name, mains, language, *numbers = record
print("Point of Contact : ", numbers)

# extracting sequence of occr in an array
sales = [10, 8, 7, 10, 11, 13, 15, 17]
*qtrs, last = sales
# this wont print  the last occurence of number
print(qtrs)

trv_avg = sum(qtrs) / len(qtrs)
print("Average of the first 7 qrts : ", trv_avg)


# * pattern to iterate over unknown pattern of strings
def do_foo(x, y):
    print('foo', x, y)


def do_bar(x):
    print('Bar', x)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


# loop and print the constructs
# here the first becomes the tag and the subsequent becomes the value
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(*args)


# throwing unwanted variables
record = ('ACME', 50, 123.45, (2, 18, 2020))
name, *_, (*_, year) = record
print("Record Name : ", name)
print('Record year : ', year)


def sum_aggr(args):
    return sum(args)


# when you want to aggregate the objects in the list
numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
firstNumber, *aggregators = numbers
print("Sum of the numbers in the list : ", sum_aggr(aggregators))


