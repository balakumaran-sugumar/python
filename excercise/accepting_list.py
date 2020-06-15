# this will accept the user input and replace the list parameter

input_list = ['', '', '']
input_index_range = range(0, 3)


def display_list():
    print("Current list : ", input_list)


# inserting the value at the position
def insert_value(idx):
    if not idx in input_index_range:
        print("Invalid input entered .. possible index : ", input_index_range)
        return False
    else:
        user_value = input("Enter the value : ")
        input_list[idx] = user_value
        return True


def accept_user_input():
    index_valid = False

    while not index_valid:
        user_index = input("Enter the index : ")
        if user_index.isdigit():
            is_idx_pass = insert_value(int(user_index))
            if not is_idx_pass:
                index_valid = False
            else:
                index_valid = True
        else:
            print("Entered value is not Digit")
            index_valid = False

    display_list()


def accept_user_iteratively():
    wish_to_continue = True

    while wish_to_continue:
        accept_user_input()
        contnu_op = input("Do you wish to continue (Y/N)")

        contnu_op = contnu_op.lower()

        if contnu_op.startswith("y"):
            wish_to_continue = True
        else:
            wish_to_continue = False


accept_user_iteratively()
