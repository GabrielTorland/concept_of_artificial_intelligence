from snake import SnakeGame
import numpy as np

snake = SnakeGame()
shortest_sequence = []


@snake.register_ai
def super_ai():
    global shortest_sequence
    if len(shortest_sequence) == 0:
        start_position = snake.get_snake_head_position()
        apple_position = snake.get_apple_position()
        directions = [['right'], ['left'], ['up'], ['down']]
        queue = [[snake.simulate_move(start_position, 'right'), 'right'],
                 [snake.simulate_move(start_position, 'left'), 'left'],
                 [snake.simulate_move(start_position, 'up'), 'up'],
                 [snake.simulate_move(start_position, 'down'), 'down']]
        running = True
        while running:
            temp_queue = []
            for sequence in queue:
                if snake.is_legal(sequence[1:]):
                    if sequence[0] == apple_position:
                        shortest_sequence = sequence
                        running = False
                        break
                    else:
                        for direct in directions:
                            new_sequence = sequence + direct
                            new_sequence[0] = snake.simulate_move(new_sequence[0], ''.join(direct))
                            if snake.is_legal(new_sequence[1:]):
                                temp_queue.append(new_sequence)

            queue = temp_queue

    return shortest_sequence.pop(0)


snake.start(use_ai=True)
