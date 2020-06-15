# this is a simple tic tac toe problem which will take the input from the user and check who will be the winner

# accepting a user input


def user_input():
    choice = ""
    acceptable_range = range(0, 2)
    acceptable = False

    while not choice.isdigit() or not acceptable:
        choice = input("Enter the number : ")
        if choice.isdigit():
            if int(choice) in acceptable_range:
                acceptable = True
        else:
            acceptable = False
            print("Invalid input entered .. try again \n")

    return int(choice)


user_choice = user_input()
print("The user has selected : ", user_choice)
