# similar to String list can be used for indexing and slicing


# initializing a list
myList = ["One", "Two", "Three", "Four"]

# lists are mutable as opposed to String
myList[0] = "I changed the list here"

print(myList)

# adding elements to the end of the list
myList.append("Five")

# removing the element from the list
# pop removes the last element from the list
element = myList.pop()
print(element)

# removing the first element of the list
firstElement = myList.pop(0)
# if you want to remove the last element we can use -1 similar to String indexing

# sorting of the elements
# the sort element does not return any value and is of void type
# python will sort the elements inline
letters = ['a', 'b', 'm', 'd']
letters.sort()
print(letters)

# reverse sorting
letters.reverse()
print(letters)














