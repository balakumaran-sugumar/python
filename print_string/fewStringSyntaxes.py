# Strings are immutable
# once the string is assigned a variable it cannot be changed later

dirctory = 'C:/ProgramFiles/Python/test'

print('C:\ProgramFiles\Python\name')

# fix for the above issues
print(r'C:\ProgramFiles\Python\name')

randomStr = 3 * 'umm' + 'ummmmmm'
print(randomStr)

randomStr1 = 'Pyth' 'On'
print(randomStr1)

text = ('this is the way to add many strings to gether'
        ' another set of random strings ')
print(text)

# print('why won't this code print')
# solution
print('why won\'t this code print')

# Step example [::] print all string [::2] print all strings but two steps
testString = "thisisfortestingthestring"
print(testString[::2])  # this is to tell the python compiler to jump two steps in the string

# reversing a string using step funtion
testString = "New String to Test"
print(testString[::-1])  # :: print all the string but -1 in the revere order

print('tinker'[1:4])


# splitting the string
splitTest = 'Testing#Split#Functionality'
print(splitTest.split("#"))


# Example of string formatting

# formatting a string
print("The {} {} {}".format("fox", "ran", "quick"))
# another way
print("The {q} {f} {b}".format(q="quick", f="fox", b="brown"))

num = 100/77
# if the number contains only a few real number then the result will be padded with spaces
print("The number is {r:10.2f}".format(r=num))

# the string literal way
print(f'The number is {num}')






