# break condition
# below construct will check for if the number is prime or not
# the logic is if the number is not divisible by any other number then its a prime

# lets check for 100 digits
# Prime is a number is a number that is divisible by itself and 1
# other are composite numbers
# example 2, 3, 5, 7, 11 are prime
# 4, 6, 8, 9, 10 are composite

# Note: Number 17 will not be included in the range calculation
for divisors in range(2, 17):
    # Number 17 will not be inclusive of the for loop
    for checkNumbers in range(2, divisors):
        # if the number is divisible by any of the divisors, it wont be a prime
        if divisors % checkNumbers == 0:
            print(checkNumbers, 'equals', divisors, '*', checkNumbers//divisors)
            break
    else:
        print("Its a Prime Number : ", divisors)


# another example of checking if the number is prime
# again to note that Python numbers are whole number and hence 10 will not be counted
for number in range(1, 10):
    if number % 2 == 0:
        print('Number is even ', number)
        continue
    print("This is a odd number ", number)
