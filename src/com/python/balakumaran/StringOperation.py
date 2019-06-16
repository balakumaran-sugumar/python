# Python String are immutable
# e.g.  word[0] = 'J' is not allowed

# if you dont want the interpreter to handle / as special character
non_escaped_character = '(c:/test/python/interpreter)'
print(non_escaped_character)

# print the number of instances before the string
num_times = 3 * 'um' + 2 * 'test'
print(num_times)

# getting the first position of the string
# index starts for 0 and so on
first_char = 'Python'
print(first_char[0])

# getting the substring of the main word
sub_set_char = first_char[0:2]
print(sub_set_char)

# all characters after the 2 characters
print(first_char[2:])

# printing the first two characters
truncate_last_two = first_char[:2]
print("Truncating the last two characters : " + truncate_last_two)

# printing all the characters except for the last one
print(first_char[:-1])

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6 -5  -4  -3  -2  -1

# this will take time to memorize
print(first_char[-6:-4])

print("Some string operation " + first_char[0])

# single quote operation
single_quote_escape = 'quote testing\''

# out of index are handled gracefully
print("out of index garaceful handling " + first_char[0:42])

# String length
string_length = "SuperSuperSuperLongString"
print(len(string_length))

# String methods : basic transformation and searching




