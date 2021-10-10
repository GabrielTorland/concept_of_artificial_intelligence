from ikt111_games import ConnectFour
import random
import time
import math

from ikt111_games.connect_four.config import PLAYER1, PLAYER2

DEPTH = 4
ALPHA = 100000000000000
BETA = -100000000000000

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

def minimax(board, depth, alpha, beta, maximizing_player, moves):
    if depth == 0: # Depth is zero.
        if  game.is_winner(PLAYER2, board): # Nice, my ai found a winning path.
            return (None, ALPHA)
        elif game.is_winner(PLAYER1, board): # Fuck, the oponent found a winning path.
            return (None, BETA)
        else: 
            return (None, game.get_heuristic(board))
    
    # Getting the new valid locations.
    valid_columns = game.get_all_valid_cols(board)
    # Sorting with respect to the lowst delta from the middle.
    middle = valid_columns[(math.floor(len(valid_columns)/2))]
    valid_columns.sort(key=lambda x: abs(x-middle))

    if maximizing_player: # Maximizing player
        value = -math.inf
        move = random.choice(valid_columns)
        # if depth == DEPTH:
        for col in valid_columns:
            moves.append(col)
            state_1 = game.simulate_moves([(move, turn(i))for i, move in enumerate(moves)])
            new_score = minimax(state_1, depth-1, alpha, beta, False, moves)[1]
            moves.pop()
            if new_score > value:
                value = new_score
                move = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return move, value
    else: # Minimizing player.
        value = math.inf
        move = random.choice(valid_columns)
        for col in valid_columns:
            moves.append(col)
            state_2 = game.simulate_moves([(move, turn(i))for i, move in enumerate(moves)])      
            new_score = minimax(state_2, depth-1, alpha, beta, True, moves)[1]
            moves.pop()
            if new_score < value:
                value = new_score
                move = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return move, value

@game.register_ai
def super_ai():
    time.sleep(0.5)
    move, value = minimax(game.game_state, DEPTH, -ALPHA, -BETA, True, [])
    print(f"value: {value}")
    return move

game.start(use_ai=True)
