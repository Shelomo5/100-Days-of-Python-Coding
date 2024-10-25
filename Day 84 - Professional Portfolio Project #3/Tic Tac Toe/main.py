# build a text-based version of the Tic Tac Toe game.

import random

# Creating a list to be the board
board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Function explains rules of the game
def start_intro():
    print("Welcome to Tic Tac Toe."
    " The goal of the game is to be the first player to place your marker (X or O) "
    "3 times consecutively (up, down, across, or diagonally) on the board to win the game\n")


# Function for player to select marker x or o
def select_marker():

    # Use input and while loop to get a valid marker choice from players
    marker_choice = ""
    while marker_choice != "X" and marker_choice != "O":
        marker_choice = input("Player 1 Do you want to be X or O: \n").upper()
    player1 = marker_choice

    if player1 == "X":
        player2 = "O"
        print("Player 2 you are O\n")
    else:
        player2 = "X"
        print("Player 2 you are X\n")
    # print(player1, player2)
    # Return assigned marker to each player
    return [player1, player2]

# Function determines which player begins
def go_first():
    # If 1 is randomly picked player 1 starts
    if random.randint(1, 2) == 1:
        # print("player 1")
        return "Player 1"

    else:
        # print("player 2")
        return "Player 2"

# Function to display board
def display_board(board):
    print('|' + board_list[1] + '|' + board_list[2] + '|' + board_list[3] + '|')
    print("-------")
    print('|' + board_list[4] + '|' + board_list[5] + '|' + board_list[6] + '|')
    print("-------")
    print('|' + board_list[7] + '|' + board_list[8] + '|' + board_list[9] + '|')


# Prompts user to enter an integer 1-9 which corresponds to a place on the board
def choosing_position(board):
    position = ""
    #  Check if integer entered is between 1-9 and if position picked is free by calling available_check function
    while position not in [1,2,3,4,5,6,7,8,9] or not available_check(board, position):
        number = input("Please enter a number 1-9 which represents where you would like to place your marker: \n")
        position = int(number)

    return position

# Function checks if a given position on board is empty and if it is returns true
def available_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False

# Associates marker with a given index position of the board (board_list)x
def marker_placement(board, marker, position):
    board[position] = marker

# Function checks if marker is the same for three positions in a row and hence player wins
def win_check(board, marker):
    if (board[1] == board[2] == board[3] == marker):
        return True
    elif (board[4] == board[5] == board[6] == marker):
        return True
    elif (board[7] == board[8] == board[9] == marker):
        return True
    elif (board[1] == board[4] == board[7] == marker):
        return True
    elif (board[2] == board[5] == board[8] == marker):
        return True
    elif (board[3] == board[6] == board[9] == marker):
        return True
    elif (board[1] == board[5] == board[9] == marker):
        return True
    elif (board[3] == board[5] == board[7] == marker):
        return True


# Function returns True if the board is full
def is_full(board):
    for position in range(1,10):
        if board[position] == " ":
            return False
    return True

# Function returns True if player wants to play again
def play_again():
    return input("Do you want to play again? Enter yes or no: \n").lower().startswith("y")

# While loop keeps restarting the code
while True:
    #  Explaining rules of the game
    start_intro()

    # Marker selected for each player
    marker_1, marker_2 = select_marker()

    # Clears board in between games
    board_list = [" "] * 10

    #  Who goes first randomly chosen
    player_turn = go_first()
    print(player_turn + " was randomly chosen to begin the game\n")

    #  Prompt user to start game
    game_on = input("Are you ready to start the game? Type Yes or No: \n")
    if game_on.lower()[0] == "y":
        game_on = True
    else:
        game_on = False

    # While start game is True run this loop
    while game_on:
        if player_turn == "Player 1":
            # Display the board function called
            display_board(board_list)

            # Choosing_position function called so that player picks a position on the board
            position_choice = choosing_position(board_list)

            # Function called to place marker on board where player 1 chose to put it
            marker_placement(board_list, marker_1, position_choice)

            # Function called to check if player 1 has won
            if win_check(board_list, marker_1):
                display_board(board_list)
                print("Player 1 has won.\n")
                game_on = False
            else:
                # If is_full returns true then game stops because board is full
                if is_full(board_list):
                    print("It's a draw, no one wins.\n")
                    # Game stops if
                    game_on = False
                else:
                    # Otherwise it's Player 2's turn
                    player_turn = "Player 2"

        #  Player 2's turn begins
        else:
            display_board(board_list)

            # Choosing_position function called so that player picks a position on the board
            position_choice = choosing_position(board_list)

            # Function called to place marker on board where player 2 chose to put it
            marker_placement(board_list, marker_2, position_choice)

            # Function called to check if player 2 has won
            if win_check(board_list, marker_2):
                display_board(board_list)
                print("Player 2 has won.\n")
                game_on = False

            else:
                # If is_full returns true then game stops because board is full
                if is_full(board_list):
                    print("It's a draw, no one winsn\n")
                    # Game stops if
                    game_on = False
                else:
                    # Otherwise it's Player 2's turn
                    player_turn = "Player 1"

    # If player doesn't want to play again break
    if not play_again():
        break

