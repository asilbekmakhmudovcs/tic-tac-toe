"""
Tic Tac Toe Player
"""

import math, copy, random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    for row in board:
        for cube in row:
            match cube:
                case "X":
                    x += 1
                
                case "O":
                    o += 1
                
                case _:
                    continue
    
    if x > o:
        return "O"
    
    elif x == o:
        return "X"
    
    else:
        raise Exception("NOT A VALID CHARACTER!")





def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    return example (a, b) => a-> row, b->cell
    """

    empty = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == None:
                empty.add((i, j))
    
    return empty


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    turn = player(board)
    board_copy = copy.deepcopy(board) 
    if board_copy[action[0]][action[1]] == None:
        board_copy[action[0]][action[1]] = turn
        return board_copy






def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    options = ["X", "O"]

    for option in options:
        
        for i, row in enumerate(board):

            # xxx
            if row[0] == row[1] == row[2] == option:
                return option
            #   x
            #   x
            #   x
            elif  board[0][i] == board[1][i] == board[2][i] == option:
                return option
            
            #   x
            #    x
            #     x
            elif board[0][0] == board[1][1] == board[2][2] == option:
                return option
            

            #     x
            #    x
            #   x
            elif board[0][2] == board[1][1] ==  board[2][0] == option:
                return option
    

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True  # when game has winner
    
    for row in board:
        if None in row:
            return False  # when there are free cells

    return True  # if it is a tie or all cells are filled

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    options = {"X": 1, "O":-1}

    for option in options:

        for i, row in enumerate(board):
            if row[0] == row[1] == row[2] == option:
                return options[option]
        
            elif board[i][0] == board[i][1] == board[i][2] == option:
                return options[option]
                
            elif board[0][0] == board[1][1] == board[2][2] == option:
                return options[option]

            elif board[0][2] == board[1][1] == board[2][0] == option:
                return options[option]
                
    # if nothing was returned, it is draw
    return 0


def minimax(board): # minimax is ai based 
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)

    if check_for_initial_state(board):
        return (1, 1)
    
    if check_for_cental_x(board):
        corner_cells = [(0, 0), (0, 2), (2, 0), (2, 2)]
        return random.choice(corner_cells)

    if terminal(board):
        return None  # Return None for tie games

    if turn == X:
        v = float("-inf")
        best_action = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return best_action
    else:
        v = float("inf")
        best_action = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float("inf")

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v


def check_for_initial_state(board):
    for row in board:
        for i in row:
            if i != None:
                return False

    return True

def check_for_cental_x(board):
    
    if board == [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, "X", EMPTY],
                 [EMPTY, EMPTY, EMPTY]]:
        return True

    return False
 
