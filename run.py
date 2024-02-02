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