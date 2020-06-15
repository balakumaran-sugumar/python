# function and methods examples
import string


def check_bool(num, low, high):
    return low <= num <= high


print("Printing the condition :", check_bool(13, 1, 10))
print("Printing the condition :", check_bool(1, 1, 10))
print("Printing the condition :", check_bool(10, 1, 10))
print("Printing the condition :", check_bool(0, 1, 10))


# the - sign finds the difference between the two set
def ispangram(str1, alphabet=string.ascii_lowercase):
    whatsHere = set(alphabet) - set(str1.lower())
    print(whatsHere)
    return not set(alphabet) - set(str1.lower())


print(ispangram("Pack my box with five dozen liquor"))

