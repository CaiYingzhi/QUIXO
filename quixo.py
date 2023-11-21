import random
import math

def check_move(board, turn, index, push_from):
    # player 1 will be represented by 1, player 2 represented by 2 and empty represented by 0 in list
    player_symbol = 1 if (turn%2) == 1 else 2
    board_width = int(math.sqrt(len(board)))
    # check if index can be chosen by player
    if not (board[index] == 0 or board[index] == player_symbol):
        return False

    # Get outer ring indexes
    top_indexes = list(range(board_width)) # 0 to board_width - 1
    last_row_first_index = board_width * (board_width - 1)
    bottom_indexes = list(range(last_row_first_index, last_row_first_index + board_width))
    left_indexes = []
    for i in range(board_width):
        left_indexes.append(i * board_width)
    right_indexes = []
    for i in range(board_width):
        right_indexes.append(i * board_width + (board_width - 1))
    
    # check if index lies in outer ring indexes
    outer_ring_indexes = [top_indexes, bottom_indexes, right_indexes, left_indexes]
    outer_ring_indexes = sum(outer_ring_indexes, []) # trick from https://stackoverflow.com/questions/3021641/concatenation-of-many-lists-in-python
    if index not in outer_ring_indexes:
        return False

    # check if can push for side
    # if left, then cannot be [x1,x2,x3] left side indexes. etc . covers the case for corner where need to push 2 directions.
    if (push_from == 'T'): # inserting from top, return False if index is in top indexes because cannot push back
        if index in top_indexes: # reuse top indexes of outer ring calculated earlier
            return False
    elif (push_from == 'B'):
        if index in bottom_indexes:
            return False
    elif (push_from == 'L'):
        if index in left_indexes:
            return False
    else: # 'R'
        if index in right_indexes:
            return False
    return True

def get_row_indexes(board_width, index):
    row_number = index // board_width # row_number: 0,1,2,3,4 etc if board_width = 5, index = 6, row number = 1
    first_index_of_row = row_number * board_width
    row_indexes = list(range(first_index_of_row, first_index_of_row + board_width))
    return row_indexes   

def get_column_indexes(board_width, index):
    column_number = index % board_width # column_number: 0,1,2,3,4 etc if board_width = 5, index = 4, column number = 4
    column_indexes = []
    for i in range(board_width):
        column_indexes.append(i * board_width + column_number)
    return column_indexes


def apply_move(board, turn, index, push_from):
    board = board[:]
    player_symbol = 1 if (turn%2) == 1 else 2 # cube taken out and to be inserted
    board_width = int(math.sqrt(len(board)))
    if (push_from == 'T'): # move within column downwards. index can be left, right or btm side
        # get column of index -> indices below of index unchanged, below on top of it have to shift down
        column_indexes = get_column_indexes(board_width, index) # eg. 0,5,10,15,20. if index == 10, only 0 and 5 shift down
        for i in reversed(range(0, board_width)): # reversed iteration of column_indexes so that shift down occurs before player cube is inserted
            if (column_indexes[i] > index):
                continue
            elif i == 0: # 1st cube in column
                board[column_indexes[i]] = player_symbol
            else:
                board[column_indexes[i]] = board[column_indexes[i-1]] # shift down
    elif (push_from == 'B'): # move within column upwards. index can be left, right or top side
        # get column of index -> indices on top of index unchanged, below ones have to rotate / shift up
        column_indexes = get_column_indexes(board_width, index) # eg. 0,5,10,15,20. if index = 10, only 15 and 20 shift up
        for i in range(board_width): # shift up occurs before player cube is inserted
            if (column_indexes[i] < index):
                continue
            elif i == board_width-1: # last row
                board[column_indexes[i]] = player_symbol
            else:
                board[column_indexes[i]] = board[column_indexes[i+1]] # shift up
    elif (push_from == 'L'): # move within row leftwards. index can be top, right or btm side
        # get row of index -> indices on right of index unchanged, those on it's left have to shift right
        row_indexes = get_row_indexes(board_width, index)
        for i in reversed(range(0, board_width)):
            if (row_indexes[i] > index):
                continue
            elif i == 0:
                board[row_indexes[i]] = player_symbol
            else:
                board[row_indexes[i]] = board[row_indexes[i-1]] # shift right
    else: # 'R'
        row_indexes = get_row_indexes(board_width, index)
        for i in range(board_width):
            if (row_indexes[i] < index):
                continue
            elif i == board_width-1:
                board[row_indexes[i]] = player_symbol
            else:
                board[row_indexes[i]] = board[row_indexes[i+1]] # shift left
    return board[:] # copy of board

def has_line(board, symbol): # check for winning criteria
    board_width = int(math.sqrt(len(board)))
    # check row for victory
    for i in range(board_width):
        row_first_index = i * board_width
        board_row = board[row_first_index:(row_first_index + board_width)]
        consecutive_symbol_count = 0
        for cube in board_row:
            # checking if ith row gives victory
            if (cube == symbol):
                # counting number of matches for given row
                consecutive_symbol_count += 1
        if (consecutive_symbol_count == board_width):
            return True

    # check column for victory
    for i in range(board_width):
        column_indexes = get_column_indexes(board_width, i)
        board_column = []
        for index in column_indexes:
            board_column.append(board[index])
        # column_match = True
        consecutive_symbol_count = 0
        for cube in board_column:
            if (cube == symbol):
                # count matches in column
                consecutive_symbol_count += 1
        if (consecutive_symbol_count == board_width):
            return True

    board_diagonal1 = [] # check diagonal \ for victory
    board_diagonal2 = [] # check diagonal / for victory
    for i in range(board_width):
        board_diagonal1.append(board[i*board_width + i])
        board_diagonal2.append(board[i*board_width + (board_width-1) - i])
    
    diagonal1_count = 0
    for cube in board_diagonal1:
        if (cube == symbol):
            diagonal1_count += 1
    if (diagonal1_count == board_width):
        return True

    diagonal2_count = 0
    for cube in board_diagonal2:
        if (cube == symbol):
            diagonal2_count += 1
    if (diagonal2_count == board_width):
        return True

    return False

def check_victory(board, who_played):
    winner = 0
    player1_has_line = has_line(board, 1) # player 1's symbol
    player2_has_line = has_line(board, 2) # player 2's symbol
    if (who_played == 1):
        if (player1_has_line):
            winner = 1
        if (player2_has_line): # special case: if player1 help player2 form line, regardless if player1 has line player2 wins
            winner = 2
    else:
        if (player2_has_line):
            winner = 2
        if (player1_has_line):
            winner = 1
    return winner

def computer_move(board, turn, level):
    computer_symbol = 1 if (turn%2) == 1 else 2
    player_symbol = 1 if computer_symbol == 2 else 2 # the computer's opponent
    board_width = int(math.sqrt(len(board)))

    # outer ring cube
    top_indexes = list(range(board_width)) # 0 to board_width - 1
    last_row_first_index = board_width * (board_width - 1)
    bottom_indexes = list(range(last_row_first_index, last_row_first_index + board_width))
    left_indexes = []
    for i in range(board_width):
        left_indexes.append(i * board_width)
    right_indexes = []
    for i in range(board_width):
        right_indexes.append(i * board_width + (board_width - 1))
    outer_ring_indexes = [top_indexes, bottom_indexes, right_indexes, left_indexes]
    outer_ring_indexes = sum(outer_ring_indexes, []) # will double count corner index
    outer_ring_indexes = list(set(outer_ring_indexes)) # turn into set then list to remove duplicates, ensuring uniqueness

    possible_directions = ['T', 'B', 'L', 'R']
    cpu_playable_moves = []
    for index in outer_ring_indexes:
        for direction in possible_directions:
            if (check_move(board, computer_symbol, index, direction)):
                cpu_playable_moves.append((index,direction))

    # level 1:
    if level == 1:
        selected_move_index = random.randint(0, len(cpu_playable_moves)-1) # randint includes endpoint
        return cpu_playable_moves[selected_move_index]

    # level 2:
    else:
        remaining_cpu_playable_moves = cpu_playable_moves[:] # copy
        # find winning move
        for i in range(len(cpu_playable_moves)):
            # loop by index vs loop by cpu_playable_moves, consider method of removing of cpu_playable_moves
            move = cpu_playable_moves[i]
            # pass in copy of board to avoid changing original. apply_move modifies the board passed to it
            cpu_move_board = apply_move(board[:], computer_symbol, get_move_index(move), get_move_direction(move))
            winner = check_victory(cpu_move_board, computer_symbol)
            if winner == computer_symbol: # use the winning move
                print('check winning move')
                print(move)
                display_board(cpu_move_board)
                return move
            elif winner == player_symbol:
                remaining_cpu_playable_moves[i] = "to remove"
                # print("check lose")
                # display_board(cpu_move_board)
                # print(remaining_cpu_playable_moves)
            # remove losing moves from cpu playable moves
            player_legal_moves = []
            for index in outer_ring_indexes:
                for direction in possible_directions:
                    if (check_move(board, player_symbol, index, direction)):
                        player_legal_moves.append((index,direction))
            for player_move in player_legal_moves:
                player_move_board = apply_move(cpu_move_board[:], player_symbol, \
                    get_move_index(player_move), get_move_direction(player_move))
                winner = check_victory(player_move_board, player_symbol)
                if winner == player_symbol:
                    remaining_cpu_playable_moves[i] = "to remove"
        # randomly select playable moves
        remaining_cpu_playable_moves = [e for e in remaining_cpu_playable_moves if e != "to remove"]
        if len(remaining_cpu_playable_moves) > 0:
            selected_move_index = random.randint(0, len(remaining_cpu_playable_moves)-1)
            return remaining_cpu_playable_moves[selected_move_index]
        else: # if no available move left, result doesn't matter. will lose anyway
            selected_move_index = random.randint(0, len(cpu_playable_moves)-1)
            return cpu_playable_moves[selected_move_index]

def display_board(board):
    board_width = int(math.sqrt(len(board)))
    board_str = ""
    for i in range(len(board)):
        if (board[i] == 0):
                board_str += ' . '
        elif (board[i] == 1):
                board_str += ' X '
        else:
                board_str += ' O '
        # board_str += str(board[i])

        if ((i+1)%board_width == 0):
            board_str += "\n"
    print(board_str)

def get_board_width():
    board_width = 5
    try:
        board_width = int(input("Enter board width, but must be larger than 3\n")) # 4 should be minimum
        if board_width < 4:
            raise Exception("Board size too small for Quixo game, using default width of 5...")
    except:
        board_width = 5
        print("You have selected an invalid board width, using default width of 5...")
    print(f"You have selected a {board_width}x{board_width} board")
    return board_width

def get_board(board_width):
    return [0] * (board_width * board_width) # 0 for blank, 1 for player 1, 2 for player 2

def check_whose_turn(turn):
    return turn % 2

def check_direction_valid(direction, directions):
    if direction in directions:
        return True
    else:
        return False

def get_move(board, board_size, turn, computer_mode, level, computer_go_first):
    player_turn = (computer_go_first and (turn%2) == 0) or ((not computer_go_first) and (turn%2) == 1)
    if ((not computer_mode) or (computer_mode and player_turn)):
        print(f"Player {turn}'s turn, choose a index from {0} to {board_size - 1}.")
        input_index = -1
        input_direction = ''
        possible_directions = ['T', 'B', 'L', 'R']
        while input_index < 0:
            if ((turn%2) == 1):
                print("only pick blank cubes in the outer ring, represented by [ ], or X")
            else:
                print("only pick blank cubes in the outer ring, represented by [ ], or O")
            try:
                player_input = int(input())
                if (player_input >= 0 and player_input < board_size):
                    input_index = player_input
            except:
                continue
        while not (check_direction_valid(input_direction, possible_directions)):
            input_direction = input("Enter direction: T, B, L or R: ")
        return (input_index, input_direction)
    else:
        return computer_move(board, turn, level)

def get_move_index(move):
    return move[0]

def get_move_direction(move):
    return move[1]

def run_game(board, board_width, computer_mode, level, computer_go_first):
    print("Player 1 will use the X symbol, Player 2 will use the O symbol")
    board_size = board_width * board_width
    turn_counter = 1 # player 1's turn is counter % 2 == 1(1,3,5,7...), player 2's turn is counter % 2 == 0 (2,4,6,8..)
    # winner = 0 # undecided
    game_ended = False
    print(f"Current turn: {turn_counter}")
    while not game_ended:
        display_board(board)
        # check who's turn and ask for move respectively
        turn = check_whose_turn(turn_counter)
        move = get_move(board, board_size, turn, computer_mode, level, computer_go_first)
        move_index = get_move_index(move)
        move_direction = get_move_direction(move)
        # check if move is valid
        legal_move_selected = False
        while not legal_move_selected:
            legal_move_selected = check_move(board, turn, move_index, move_direction)
            if legal_move_selected:
                break
            else:
                print("Invalid move")
                move = get_move(board, board_size, turn, computer_mode, level, computer_go_first)
                move_index = get_move_index(move)
                move_direction = get_move_direction(move)
        # apply valid move
        if computer_mode:
            if (computer_go_first and (turn%2) == 1) or (not computer_go_first and turn%2 == 0):
                print(f"Computer chooses {move_index} and push from {move_direction}")
        board = apply_move(board, turn, move_index, move_direction)
        # check victory
        who_played = 1 if (turn%2) == 1 else 2
        who_win = check_victory(board, who_played)
        game_ended = True if who_win != 0 else False
        if game_ended:
            display_board(board)
            print(f"Player {who_win} has won! Total {turn_counter} turns taken!")
        turn_counter += 1

def run_computer_mode():
    print("You have selected to play against the computer")
    board_width = get_board_width()
    board = get_board(board_width)
    level = 1
    try:
        input_result = int(input("Computer level (Enter 1 or 2): "))
        if input_result == 1 or input_result == 2:
            level = input_result
            print(f"Starting level {level}.")
        else:
            level = 1
            print("Invalid input, starting level 1 by default")
    except:
        print("Invalid input, starting level 1 by default")
    computer_go_first = False
    try:
        input_result = int(input("Enter 1 if you want computer to be player 1 and start first: "))
        if input_result == 1:
            computer_go_first = True
    except:
        print("Invalid input, you can be player 1 and start first")
    run_game(board, board_width, True, level, computer_go_first)

def run_player_mode():
    print("You have selected to play against another player")
    board_width = get_board_width()
    board = get_board(board_width)
    run_game(board, board_width, False, 0, False)

def menu():
    # Variables for clarity
    computer_mode = 1
    player_mode = 2

    # Variables for reuse
    enter_opponent_prompt = "Enter 1 if you want to play against computer. Enter 2 if you want to play against player\n"

    print("Welcome to quixo")
    
    game_mode = 0
    while not (game_mode == computer_mode or game_mode == player_mode):
        try:
            game_mode = int(input(enter_opponent_prompt))
        except:
            continue

    if game_mode == computer_mode:
        run_computer_mode()
    else:
        run_player_mode()

if __name__ == "__main__":
    menu()


    
