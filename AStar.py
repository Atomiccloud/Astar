from math import sqrt, inf
from Node import Node
import heapq as h
from DisplayGUI import GUI
import time


def onSeg(p, q, r):
    if (min(p[0], r[0]) >= q[0] > max(p[0], r[0])) and (min(p[1], r[1]) >= q[1] > max(p[1], r[1])):
        return True
    return False


def ccw(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0:
        return val
    return 1 if val > 0 else 2


def intersect(p1, p2, p3, p4):
    ccw1, ccw2, ccw3, ccw4 = ccw(p1, p2, p3), ccw(p1, p2, p4), ccw(p3, p4, p1), ccw(p3, p4, p2)

    if ccw1 != ccw2 and ccw3 != ccw4:
        return True

    if ccw1 == 0 and onSeg(p1, p3, p2):
        return True
    if ccw2 == 0 and onSeg(p1, p4, p2):
        return True
    if ccw3 == 0 and onSeg(p3, p1, p4):
        return True
    if ccw4 == 0 and onSeg(p3, p2, p4):
        return True

    return False


def getChildren(node, v, e, shape):
    children = []
    for point in v:
        intersected = False
        for edge in e:
            # check if intersects
            if intersect(node.position, point, edge[0], edge[1]) and point not in edge and node.position not in edge:
                intersected = True
        if not intersected and node.position != point:
            # check if point is in shape and adjacent
            dissects_shape = False
            for shpe in shape:
                if point in shpe and node.position in shpe:
                    if point == shpe[-1]:
                        if not (node.position == shpe[-2] or node.position == shpe[0]) and point not in children:
                            dissects_shape = True
                    elif not (node.position == shpe[shpe.index(point) + 1] or node.position == shpe[
                        shpe.index(point) - 1]):
                        dissects_shape = True
            if point not in children and not dissects_shape:
                children.append(point)
    return children


def ED(point, end):
    return sqrt(((point[0] - end[0]) ** 2) + ((point[1] - end[1]) ** 2))


class AStar:
    def __init__(self, v, e, shape):
        self.v = v
        self.e = e
        self.shape = shape

    def astar(self, start, end, user_input):
        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0
        g = inf
        w = 101
        incumbent = []

        # Initialize open list
        open_list = []

        # Add the start node
        h.heappush(open_list, (start_node.f, start_node))

        # Loop until you find the end
        finished = False
        while len(open_list) > 0 and not finished:
            if w == 1:
                finished = True
            newSolution = self.improveAstar(open_list, w, g, end_node, start)
            if newSolution is not None:
                g = newSolution[1]
                incumbent = newSolution[0]
                GUI(incumbent, self.v, False, user_input)
            else:
                return incumbent

            if w > 1:
                w = w - 10

            for node in open_list:
                if node[1].f >= g:
                    open_list.pop(open_list.index(node))

        return incumbent

    def improveAstar(self, open_list_inc, w, g, end_node, start):
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        closed_list = []
        open_list = open_list_inc

        h.heappush(open_list, (start_node.f, start_node))

        while len(open_list) > 0:
            # Get the current node
            current_node = h.heappop(open_list)[1]
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1], current_node.g

            # gets points that we can go to
            children = getChildren(current_node, self.v, self.e, self.shape)

            # add children nodes to open list
            for point in children:
                child_node = Node(current_node, point)

                # calculate scores
                child_node.g = ED(current_node.position, point) + current_node.g
                child_node.h = ED(point, end_node.position)
                child_node.f = child_node.g + (child_node.h * w)

                # check if node in open or closed list
                for node in open_list:
                    if child_node == node[1] and child_node.g > node[1].g:
                        continue

                for node in closed_list:
                    if child_node == node:
                        continue

                h.heappush(open_list, (child_node.f, child_node))
        return None
