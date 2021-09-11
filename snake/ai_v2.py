from ikt111_games import Snake
import random

snake = Snake()
shortest_sequence = []


class Node:
    def __init__(self, pos, parent, move):
        self.pos = pos
        self.move = move
        self.parent = parent

    def find_sequence(self):
        sequence = []
        CurrentNode = self
        while CurrentNode.parent is not None:
            sequence.append(CurrentNode.move)
            CurrentNode = CurrentNode.parent
        return sequence[::-1]


def bfs():
    global shortest_sequence
    apple_position = snake.get_apple_position()
    current_position = snake.get_snake_head_position()
    directions = {'right', 'left', 'up', 'down'}
    opposite_directions = {
        'right': 'left',
        'left': 'right',
        'up': 'down',
        'down': 'up'
    }
    queue =[Node(pos=current_position, parent=None, move=random.choice(list(directions)))]
    visited = set()
    running = True
    while running and len(queue) != 0:
        temp_queue = []
        for node in queue:
            if node.pos == apple_position:
                shortest_sequence = node.find_sequence()
                running = False
                break
            else:
                for direct in (directions - {opposite_directions[node.move]}):
                    pos_ = snake.simulate_move(node.pos, direct)
                    pos = (pos_[0], pos_[1])
                    if pos not in visited:
                        if snake.is_legal(node.find_sequence() + [direct]):
                            visited.add(pos)
                            temp_queue.append(Node(pos=pos_, parent=node, move=direct))
        if len(temp_queue) == 0:
            for move in directions:
                if snake.is_legal(move):
                    shortest_sequence = [move]
                    break
            if len(shortest_sequence) == 0:
                # No possible moves, snake is dead.
                shortest_sequence = [random.choice(list(directions))]
            running = False
        else:
            queue = temp_queue
        visited = set()


@snake.register_ai
def super_ai():
    global shortest_sequence
    if len(shortest_sequence) == 0:
        bfs()
    return shortest_sequence.pop(0)


snake.start(use_ai=True)
