# Import libraries used for 'randint' method
import random

# Gameboards - 4 needed for the game to run
PLAYER1_BOARD = [[" "] * 7 for i in range(7)]
COMPUTER_BOARD = [[" "] * 7 for i in range(7)]
PLAYER1_CHOICE = [[" "] * 7 for i in range(7)]
COMPUTER_CHOICE = [[" "] * 7 for i in range(7)]

# Size of each vessel in gameboard area
VESSEL_SIZE = [1, 1, 2, 2, 3,]

# Welcome screen message - battleship art from ansi art website
def welcome_message():
    print("""

    ____        __  __  __          __    _           
   / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___  _____
  / __  / __ `/ __/ __/ / _ \/ ___/ __ \/ / __ \/ ___/
 / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ (__  ) 
/_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/____/  
                                       /_/            

                """)

# Info for player - rules and game details
    print("Are you ready to battle? Here are some rules before we begin:")
    print("\n")
    print("Your field of battle is made up of a 7x7 grid.")
    print("\n")
    print("The ships at your disposal - and their allocated spacing.")
    print("\n")
    print("Single soldier boat - 1 space")
    print("\n")
    print("Submarine - 2 spaces ")
    print("\n")
    print("Battleship - 3 spaces")
    print("\n")
    print("Be the first player to sink all of the opponents ships")
    print("\n")

# Code used to create gameboard
def display_board(board):
    print("===== BATTLESHIP Board =====")
    print("\n")
    print("  1 2 3 4 5 6 7")
    print("  -------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print("\n")

# Code for placing ships - a function that will loop through the different
# available vessels and check for any issues with overlaps

def ship_location(board):
    for ship_size in VESSEL_SIZE:
        while True:
            if board == COMPUTER_BOARD:
                position, row, column = random.choice(["S", "U"]), \
                    random.randint(0, 6), random.randint(0, 6)
                if check_position(ship_size, row, column, position):
                    if not overlap_monitor(board, row, column, position,
                                         ship_size):
                        if position == "S":
                            for i in range(column, column + ship_size):
                                board[row][i] = "@"
                        elif position == "U":
                            for i in range(row, row + ship_size):
                                board[i][column] = "@"
                        break
            else:
                ship_location = True
                print("Place vessel that is alloted to this many space(s):"
                + str(ship_size))
                row, column, position = player1_coordinates(ship_location)
                if check_position(ship_size, row, column, position):
                    if overlap_monitor(board, row, column, position,
                                     ship_size):
                        print("\n")
                        print("Vessel can not be placed here. Try again!\n")
                    else:
                        if position == "S":
                            for i in range(column, column + ship_size):
                                board[row][i] = "@"
                        elif position == "U":
                            for i in range(row, row + ship_size):
                                board[i][column] = "@"
                        else:
                            break
                        display_board(PLAYER1_BOARD)
                        break
                        print("\n")

# Code for inserting coordinates for both 
# attacking computers vessels and placing your own

def player1_coordinates(ship_location):

    if ship_location == True:
        while True:
            try:
                position = input("Upright(U) or Sideways(S)?\n")\
                                  .upper()
                if position == "S" or position == "U":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Enter valid input either:(U or S)\n")
        while True:
            try:
                row = input("Row - between 1-7:\n")
                if row in "1234567":
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Enter valid input between 1-7:\n")
        while True:
            try:
                column = input("Column - between 1-7:\n").upper()
                if column not in "1234567":
                    print("Enter valid input between 1-7:\n")
                else:
                    column = int(column) - 1
                    break
            except KeyError:
                print("Enter valid input between 1-7:\n")
        return row, column, position
    else:
        while True:
            try:
                row = input("Row - between 1-7:\n")
                if row in "1234567":
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Enter valid input between 1-7:\n")
        while True:
            try:
                column = input("Column - between 1-7:\n").upper()
                if column not in "1234567":
                    print("Enter valid input between 1-7:\n")
                else:
                    column = int(column) - 1
                    break
            except KeyError:
                print("Enter valid input between 1-7:\n")
        return row, column

# Code for checking if there is any overlap with existing placements by
# looking for the "@" symbol we used to represent our vessels

def overlap_monitor(board, row, column, position, ship_size):
    if position == "S":
        for i in range(column, column + ship_size):
            if board[row][i] == "@":
                return True
    else:
        for i in range(row, row + ship_size):
            if board[column][i] == "@":
                return True
    return False

# Code for checking position of the vessel
# if its within the area of the board and if
# it comes back as false an error message is generated

def check_position(SHIP_SIZE, row, column, position):
    
    if position == "S":
        if column + SHIP_SIZE > 7:
            return False
        else:
            return True
    else:
        if row + SHIP_SIZE > 7:
            return False
        else:
            return True

# Code for going between computer and player1 turns.
# Shows when a vessel has been hit or not
# and uses randint to make computers guess random

def player1_computer_turns(board):

    if board == PLAYER1_CHOICE:
        row, column = player1_coordinates(PLAYER1_CHOICE)
        if board[row][column] == "-":
            player1_computer_turns(board)
        elif board[row][column] == "X":
            player1_computer_turns(board)
        elif COMPUTER_BOARD[row][column] == "@":
            board[row][column]
            print("Hit!\n")
        else:
            board[row][column] = "-"
            print("Missed!\n")
    else:
        row, column = random.randint(0, 6), random.randint(0, 6)
        if board[row][column] == "-":
            player1_computer_turns(board)
        elif board[row][column] == "X":
            player1_computer_turns(board)
        elif PLAYER1_BOARD[row][column] == "@":
            board[row][column]
            print("We have been hit!\n")
        else:
            board[row][column] = "-"
            print("They missed!\n")