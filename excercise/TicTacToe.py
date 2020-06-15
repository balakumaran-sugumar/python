# creating a tic tak toe program
import random

board_pts = ['', '', '', '', '', '', '', '', '']
player1 = ''
player2 = ''
unaccoupied_index = []


def print_board():
    print_stmt = "| "
    count = 1
    print("x" * 50)
    if not unaccoupied_index:
        for index, value in enumerate(board_pts):
            unaccoupied_index.append(index)

    for points in board_pts:
        print_stmt = print_stmt + points + " | "
        if count % 3 == 0:
            print(print_stmt)
            print_stmt = "| "
        count = count + 1
    print("x" * 50)


def insert_value(index, inserted_value, autobot):
    valid_values = ['X', 'O']

    inserted_value = inserted_value.upper()

    if inserted_value not in valid_values:
        print("Incorrect value : ", inserted_value)
        return False
    elif board_pts[index]:
        if not autobot:
            print("This is already marked! Select another index")
        return False
    else:
        board_pts[index] = inserted_value
        print_board()
        return True


def accept_inserted_value(value, autobot):
    success_insert = False

    if autobot:
        rand_index = random.randrange(len(unaccoupied_index))
        index = unaccoupied_index[rand_index]
    else:
        index = input("Enter the index (0-9) : ")
        if not index.isdigit() and index is not range(0, 9):
            print("Invalid digit entered, should be in range of 0-9")
            return False

    while not success_insert and autobot:
        success_insert = insert_value(int(index), value, autobot)
    else:
        insert_value(int(index), value, autobot)
    unaccoupied_index.remove(int(index))


def init_game():
    accepted_input = ['X', 'O']
    init_player_mark = input("Player1 select X/O : ").upper()
    global player2, player1

    if init_player_mark not in accepted_input:
        print("Invalid option selected")
    else:
        player1 = init_player_mark
        accepted_input.remove(player1)
        player2 = accepted_input.pop()
        accept_inserted_value(player1, False)

    loop_through()


def check_for_win(player):

    contains_blank = False
    global board_pts
    win = True

    for elements in board_pts:
        if elements == '':
            contains_blank = True

    if not contains_blank:
        print("Its a tie !!!")
        return True

    # check if the horizontal row match
    return ((board_pts[6] == player and board_pts[7] == player and board_pts[8] == player) or  # across the top
            (board_pts[3] == player and board_pts[4] == player and board_pts[5] == player) or  # across the middle
            (board_pts[0] == player and board_pts[1] == player and board_pts[2] == player) or  # across the bottom
            (board_pts[6] == player and board_pts[3] == player and board_pts[0] == player) or  # down the left side
            (board_pts[7] == player and board_pts[4] == player and board_pts[1] == player) or  # down the middle
            (board_pts[8] == player and board_pts[5] == player and board_pts[2] == player) or  # down the right side
            (board_pts[6] == player and board_pts[4] == player and board_pts[2] == player) or  # diagonal
            (board_pts[8] == player and board_pts[4] == player and board_pts[0] == player))  # diagonal


def loop_through():
    player_chance = 2
    success = False
    while not success:
        if player_chance == 1:
            print("Player 1 : ")
            accept_inserted_value(player1, False)
            player_chance = 2
            success = check_for_win(player1)
            if success:
                print("\n\n" + "$$$"*15 + " Player 1 wins " + "$$$"*15 + "\n\n")
        else:
            print("Auto Bot playing ... \n\n")
            accept_inserted_value(player2, True)
            player_chance = 1
            success = check_for_win(player2)
            if success:
                print("\n\n" + "$$$"*15 + " Auto Bot wins " + "$$$"*15 + "\n\n")


print(" **** Welcome to Tic Tac Toe game **** ")

print_board()

init_game()
