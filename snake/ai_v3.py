from ikt111_games import Snake
import random

snake = Snake()


# Class for each node.
class Node:
    def __init__(self, pos, move, parent, g, h):
        self.pos = pos
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def find_sequence(self):
        sequence = []
        CurrentNode = self
        while CurrentNode.parent is not None:
            sequence.append(CurrentNode.move)
            CurrentNode = CurrentNode.parent
        return sequence[::-1]


# Checks if the position sent in is in the list of objects sent in.
def check_visited(lst, pos):
    for node in lst:
        if node.pos == pos:
            return True
    return False


# Checking if g is larger then the g's in the open list.
def check_g(open_list, new_g):
    for node in open_list:
        if new_g > node.g:
            return True
    return False


# A* algorithm, finding the shortest path.
def a_star():
    apple_position = snake.get_apple_position()
    starting_position = snake.get_snake_head_position()
    directions = ['right', 'left', 'up', 'down']

    # Starting with f = 0
    open_list = [Node(pos=starting_position, parent=None, move=random.choice(directions), g=0, h=0)]
    closed_list = set()
    while len(open_list) != 0:

        # Choosing the current node with the smallest f.
        node = min(open_list, key=lambda x: x.f)
        open_list.remove(node)

        # Moving the nodes with smallest f to the closed list.
        # These nodes get children first, kind of a natural selection.
        closed_list.add(node)
        if node.pos == apple_position:
            # Returning shortest sequence when apple is found.
            return node.find_sequence()
        else:
            # Moves from starting point to the current node.
            current_sequence = node.find_sequence()

            # Producing children for the current node.
            for direct in directions:

                # Simulating the next move, and getting the new position.
                pos = snake.simulate_move(node.pos, direct)

                # If the child's position is in closed list we skip.
                # We cant remove any nodes in the closed list because they got children.
                if check_visited(closed_list, pos):
                    continue

                # Checks if the child is in the open list.
                elif check_visited(open_list, pos):

                    # If this child is further away from the start position then any nodes in the open list we skip.
                    if check_g(open_list, node.g+1):
                        continue
                # Checks if the move is legal.
                if snake.is_legal(current_sequence + [direct]):

                    # Adding new node to open list.
                    open_list.append(Node(pos=pos, parent=node, move=direct, g=(abs(pos[0] - starting_position[0]) +
                                                                                abs(pos[1] - starting_position[1])),
                                          h=(node.h + 1)))
    return [random.choice(directions)]


@snake.register_ai
def super_ai():
    shortest_sequence = []
    if len(shortest_sequence) == 0:
        shortest_sequence = a_star()
    return shortest_sequence.pop(0)


snake.start(use_ai=True)
