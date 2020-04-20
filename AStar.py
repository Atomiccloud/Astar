from math import sqrt, inf
from Node import Node


def ED(point, end):
    return sqrt(((point[0] - end[0]) ** 2) + ((point[1] - end[1]) ** 2))


def astar(grid, start, end, size):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    g = inf
    w = 51
    incumbent = []

    open_list = [start_node]

    # Loop until you find the end
    finished = False
    while len(open_list) > 0 and not finished:
        if w == 1:
            finished = True
        newSolution = improve_astar(open_list, w, end_node, start_node, grid)
        if newSolution is not None:
            g = newSolution[1]
            incumbent = newSolution[0]
            print(incumbent)
            #GUI(grid, incumbent, size)
        else:
            return incumbent

        if w > 1:
            w = w - 10
            open_list = [start_node]

        for node in open_list:
            if node.f >= g:
                open_list.pop(open_list.index(node))

    return incumbent


def improve_astar(open_list, w, end, start, grid):
    # Create start and end node
    start_node = start
    start_node.g = start_node.h = start_node.f = 0
    end_node = end
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = open_list
    closed_list = []

    # Add the start node

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], current_node.g  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(grid[len(grid) - 1]) - 1) or node_position[1] < 0:
                continue

            if grid[node_position[0]][node_position[1]] != 0:
                continue

            child_node = Node(current_node, node_position)

            # Append
            children.append(child_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = ED(current_node.position, child.position) + current_node.g
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + (child.h * w)

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node:
                    if child.g >= open_node.g:
                        continue
                    else:
                        child.g = open_node.g

            # Add the child to the open list
            open_list.append(child)

    return None
