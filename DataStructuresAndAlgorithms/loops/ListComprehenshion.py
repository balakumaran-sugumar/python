# short hand for flattening the list and adding it to the new list

myList = [lit for lit in range(0, 100)]

print(myList)

# more on initialization

myList = [x for x in range(1, 50) if(x % 2 == 0)]

print("This should be only even numbers : ", myList)

# celcuis to f
celcuis = [0, 10, 20, -10, 30, -40]

fList = [((9/5)*cel + 32) for cel in celcuis]

print("Temperature in F", fList)

