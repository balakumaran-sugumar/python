# defining a function that will take in a user-address and pin
def addAddress(userAddress, pin):
    print('Added the new address : ', userAddress)


# this input user-address and pin
userAddress = 'WashingtonDC USA'
pin = '123456'

# calling a function
addAddress(userAddress, pin)

# this will give the the index value of the word U
print(userAddress.index("U"))
# this will replace the character with blank space
print(userAddress.replace("A", ""))
