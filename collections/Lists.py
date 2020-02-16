import math
import statistics

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

def avgOutMarks(grades):
    first, *middle, last = grades
    return statistics.mean(middle)


# printing out the average
grades = [1, 40, 38, 39, 40, 43, 45, 44, 48, 2]
print("Average of the middle marks : ", avgOutMarks(grades))

# example of assigning multiple phone numbers of a person
record = ['Bala', 'Computer Science', 'Python', '413-407-8334', '412-405-7756']
name, mains, language, *numbers = record
print("Point of Contact : ", numbers)


