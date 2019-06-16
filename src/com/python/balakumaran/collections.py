# lists are mutable and can be changed

# list declaration
# length starts from 0
lists = [10, 20, 30, 40]
print(lists[2])

# printing the last number
print(lists[-1])

lists = lists + [50, 60, 70, 80, 90]
print(lists)

# we can append more values
lists.append(100)
print(lists)

# alphabets
alphabets = ['a', 'b', 'c', 'd', 'e']
print("Current alphabet list : ")
print(alphabets)

# replace the c and d with C and D
alphabets[2:3] = ['C', 'D']
print("Printing modified string : ")
print(alphabets)

print(len(alphabets))

# list can be nested, this becomes a matrix
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = [list1, list2]
print(list3[0][1])








