from ikt111_games import ConnectFour
from ikt111_games.connect_four.config import PLAYER1, PLAYER2
import time
import random
import math

DEPTH = 4
ALPHA = 100000000000000

game = ConnectFour()

def turn(index):
    if (index+1) % 2 == 0:
        return PLAYER1
    else:
        return PLAYER2

# get_heuristic : Calculate a heuristic given a state.
# is_winning : Checks if a given player wins the game in a given game state
# get_all_valid_cols : This function will return all valid columns given a state
# simulate_moves : Simulates a sequence of moves

def calculate_move(board, depth, alpha, moves):
    if depth == 0: # Depth is zero.
        if  game.is_winner(PLAYER2, board): # Nice, my ai found a winning path.
            return None, ALPHA
        else: 
            return None, game.get_heuristic(board)
    # Getting the new valid locations.
    valid_columns = game.get_all_valid_cols(board)
    # Sorting with respect to the lowst delta from the middle.
    middle = valid_columns[(math.floor(len(valid_columns)/2))]
    valid_columns.sort(key=lambda x: abs(x-middle))

    value = -math.inf 
    move = random.choice(valid_columns)
    for col in valid_columns:
        moves.append(col)
        moves.append(random.choice(valid_columns))
        state = game.simulate_moves([(move, turn(i))for i, move in enumerate(moves)])
        new_score = calculate_move(state, depth-1, alpha, moves)[1]
        moves.pop()
        moves.pop()
        if new_score > value:
            value = new_score
            move = col
    return move, value

@game.register_ai
def super_ai():
    return calculate_move(game.board_piece, DEPTH, -ALPHA, [])[0]

game.start(use_ai=True)