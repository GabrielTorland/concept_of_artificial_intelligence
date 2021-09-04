import math, random

snake = SnakeGame()
last_direction = None


@snake.register_ai
def super_ai():
    global last_direction
    # Getting coordinates of snakes head and apple.
    head_y, head_x = snake.get_snake_head_position()
    apple_y, apple_x = snake.get_apple_position()

    next_moves = [(head_x + 1, head_y, 'down'), (head_x, head_y - 1, 'left'), (head_x - 1, head_y, 'up'),
                  (head_x, head_y + 1, 'right')]

    # Deleting the opposite move of the last move to prevent the snake to go into itself.
    if last_direction is not None:
        rem = {}
        opposite_dir = {'left': 'right',
                        'right': 'left',
                        'up': 'down',
                        'down': 'up'
                        }
        for move in next_moves:
            rem[move[2]] = move
        next_moves.remove(rem[opposite_dir[last_direction]])

    x_, y_, direction_ = random.choice(next_moves)
    state = True
    smallest_distance = (math.sqrt((apple_x-x_)**2 + (apple_y-y_)**2), direction_)

    for x, y, direction in next_moves:
        new_distance = math.sqrt((apple_x - x) ** 2 + (apple_y - y) ** 2)
        if smallest_distance[0] > new_distance and snake.is_legal(direction):
            smallest_distance = (new_distance, direction)
            state = False
    if state and snake.is_legal(smallest_distance[1]) is not True:
        for move in next_moves:
            if snake.is_legal(move[2]):
                smallest_distance = (None, move[2])
                break
    last_direction = smallest_distance[1]
    return str(smallest_distance[1])


snake.start(use_ai=True)
