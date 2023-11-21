from quixo import *

# Check move

board = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if not check_move(board, 1, 5, 'R'):
    print("test check_move 5 - OK !")  # allowed move
else:
    print("test check_move 5 - Problem in the check_move function output !")

board = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# if not check_move(board, 1, 26, 'R'):
#     print("test check_move 7 - OK !")  # 26 is out of bounds
# else:
#     print("test check_move 7 - Problem in the check_move function output !")


# Check Victory
board = [1, 2, 0, 1, 0, 2, 1, 0, 2, 2, 0, 1, 2, 1, 0, 2, 2, 1, 0, 1, 2, 0, 1, 1, 2]
if check_victory(board, 1) == 2:
    print("test check_victory 5 - OK !")  # 2 wins diagonal
else:
    print("test check_victory 5 - Problem in the check_victory function output !")

# Computer moves
print()

board = [1, 1, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 2, 2, 2, 2, 0, 0, 1, 2, 1, 0, 0, 0, 2]
if computer_move(board, 1, 2) in [(0, 'R')]:
    print("test computer_move 1 - OK !")  # blocks player 2 column 5 win
else:
    print("test computer_move 1 - Problem in the computer_move function output !")

board = [0, 0, 2, 2, 2, 0, 1, 1, 0, 2, 2, 0, 1, 2, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1]
if computer_move(board, 1, 2) in [(20, 'T')]:
    print("test computer_move 2 - OK !")  # direct diagonal win
else:
    print("test computer_move 2 - Problem in the computer_move function output !")

