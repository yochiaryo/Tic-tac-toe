import random
import time


board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# Function to show the board
def show_board(list_name):
    print(f'''
{list_name[0]} | {list_name[1]} | {list_name[2]}       1 | 2 | 3
{list_name[3]} | {list_name[4]} | {list_name[5]}       4 | 5 | 6
{list_name[6]} | {list_name[7]} | {list_name[8]}       7 | 8 | 9
''')


# Checks all winning situations
def has_won(list_name, mark):
    if all(i == f"{mark}" for i in list_name[:3]):
        return True
    elif all(i == f"{mark}" for i in list_name[3:6]):
        return True
    elif all(i == f"{mark}" for i in list_name[6:9]):
        return True
    elif all(i == f"{mark}" for i in (list_name[0], list_name[3], list_name[6])):
        return True
    elif all(i == f"{mark}" for i in (list_name[1], list_name[4], list_name[7])):
        return True
    elif all(i == f"{mark}" for i in (list_name[2], list_name[5], list_name[8])):
        return True
    elif all(i == f"{mark}" for i in (list_name[0], list_name[4], list_name[8])):
        return True
    elif all(i == f"{mark}" for i in (list_name[2], list_name[4], list_name[6])):
        return True
    else:
        return False


# Adds either an X or an O to the board
def add_mark(list_name, user_number, mark):
    while True:
        try:
            user = int(input(f"User {user_number}: Choose position:\n"))
            if user in range(1, 10):
                if list_name[int(user) - 1] == "-":
                    list_name[int(user) - 1] = f"{mark}"
                else:
                    print("Position occupied.")
                    show_board(board)
                    add_mark(list_name, user_number, mark)
                return False
            else:
                print("Invalid response. Try again.")
        except ValueError:
            print("Invalid response. Try again.")


# Checks if the board has any empty spaces left, if it does not, and none of the winning situations are met from
# the has_won function, then it's a draw
def not_empty(list_name):
    if "-" not in list_name:
        show_board(board)
        print("It's a draw!")
        return False
    elif "-" in list_name:
        return True


# The player vs. player gameplay
def game():
    while True:
        if not not_empty(board):
            return False
        show_board(board)
        add_mark(board, "1", "X")
        if has_won(board, "X"):
            show_board(board)
            print("Player 1 won")
            return False
        if not not_empty(board):
            return False
        show_board(board)
        add_mark(board, "2", "O")
        if has_won(board, "O"):
            show_board(board)
            print("Player 2 won")
            return False



def bot_player(mark):
    while True:
        bot_num = random.randint(0, 8)
        if board[bot_num] == "-":
            board[bot_num] = f"{mark}"
            return False
        else:
            bot_player(mark)
            return False


# The player vs. bot gameplay
def bot_mode_1():
    while True:
        if not not_empty(board):
            return False
        show_board(board)
        add_mark(board, "1", "X")
        if has_won(board, "X"):
            show_board(board)
            print("The player has won")
            return False
        if not not_empty(board):
            return False
        show_board(board)
        print("The bot's turn:")
        time.sleep(1)
        bot_player("O")
        if has_won(board, "O"):
            show_board(board)
            print("The bot has won")
            return False


# The bot vs. player gameplay
def bot_mode_2():
    while True:
        if not not_empty(board):
            return False
        show_board(board)
        print("The bot's turn:")
        time.sleep(1)
        bot_player("X")
        if has_won(board, "X"):
            show_board(board)
            print("The bot has won")
            return False
        if not not_empty(board):
            return False
        show_board(board)
        add_mark(board, "2", "O")
        if has_won(board, "O"):
            show_board(board)
            print("The player has won")
            return False


def gameplay():
    game_mode = input(f'''
Choose game mode:
1. Player vs. player
2. Player vs. bot
3. Bot vs. player\n''')
    if game_mode == "1":
        game()
        while True:
            play_again = input("Would you like to play again?(y/n):\n").upper()
            if play_again == "Y":
                global board
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                gameplay()
            elif play_again == "N":
                return quit()
            else:
                print("Please provide a valid response.")
    elif game_mode == "2":
        bot_mode_1()
        while True:
            play_again = input("Would you like to play again?(y/n):\n").upper()
            if play_again == "Y":
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                gameplay()
            elif play_again == "N":
                return quit()
            else:
                print("Please provide a valid response.")
    elif game_mode == "3":
        bot_mode_2()
        while True:
            play_again = input("Would you like to play again?(y/n):\n").upper()
            if play_again == "Y":
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                gameplay()
            elif play_again == "N":
                return quit()
            else:
                print("Please provide a valid response.")
    else:
        print("Please provide a valid response.")
        gameplay()


def start_game():
    play = input("Would you like to play?(y/n):\n").upper()
    if play == "Y":
        gameplay()


start_game()
