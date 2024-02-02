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
                        print("\n"

