# Name this file to assignment1.py when you submit

class node:
    def __init__(self, x, y, label, parent=None, path_cost=0, h=0, isObstacle=False, isHazard=False):
        self.x = x
        self.y = y
        self.label = label


def heuristic(curr_node, goal_node):
    D = 1  # simple move cost of 1
    dx = abs(curr_node.x - goal_node.x)
    dy = abs(curr_node.y - goal_node.y)
    return D * (dx + dy)


def neighbourhood(graph, leaf):
    neighbours = []
    for next_node in graph:
        # Only append nodes that are directly left or right of
        # current node
        if (heuristic(leaf, next_node) == 1 and leaf != next_node):
            neighbours.append(next_node)
    return neighbours


def graph_search(graph, start_node, goal_node):
    frontier = []
    frontier.append(start_node)
    explored = []

    while True:
        if frontier == []:
            return False
        leaf = frontier.pop()
        if leaf == goal_node:
            return leaf.path()  # TODO: Backtrack through parents
        explored.append(leaf)
        for next_node in neighbourhood(graph, leaf):
            curr_path_cost = leaf.path_cost + 1
            if ((next_node not in frontier and next_node not in explored)
                    or (next_node in frontier and curr_path_cost < next_node.path_cost)):
                next_node.parent = leaf
                next_node.path_cost = curr_path_cost
                frontier.append(next_node)


def pathfinding(input_filepath):
    # input_filepath contains the full path to a CSV file with the input grid
    graph = []
    count_x = 0
    count_y = 0

    with open(input_filepath, "r") as inputs:
        tmp = inputs.read().split("\n")
        tmp.remove('')
        array = [i.split(",") for i in tmp]

    for row in array:
        for item in row:
            graph.append(node(count_x, count_y, item))
            count_x += 1
        count_y += 1
        count_x = 0
    for obj in graph:
        if(obj.label == "S"):
            start_node = obj
        elif(obj.label == "G"):
            goal_node = obj
        elif(obj.label == "X"):
            obj.isObstacle = True
        elif(obj.label == "H"):
            obj.isHazard = True

    # convert all tiles adjacent to a hazard to an obstacle
    for obj in graph:
        if(obj.label == "H"):
            hazard_neighbours = neighbourhood(graph, obj)
            for neighbour in hazard_neighbours:
                neighbour.label = "X"
            obj.label = "X"

    for obj in graph:
        if(obj.label is not "X"):
            obj.h = heuristic(obj, goal_node)

    graph_search(graph, start_node, goal_node)

    # optimal_path is a list of tuples indicated the optimal path from start to goal
    # explored_list is the list of nodes explored during search
    # optimal_path_cost is the cost of the optimal path from the start state to the goal state


pathfinding("input.txt")
