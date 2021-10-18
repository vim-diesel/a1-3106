# Name this file to assignment1.py when you submit  

class node:
    def __init__(self, x, y, label, parent=None, path_cost=0, h=0):
        self.x = x
        self.y = y
        self.label = label
        self.path_cost = path_cost
        self.parent = parent
        self.h = h

def f_n(node):
    return node.path_cost + node.h

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
        # skip obstacles ("X")
        if(next_node.label != "X"):
            if (heuristic(leaf, next_node) == 1 and leaf != next_node):
                neighbours.append(next_node)
    return neighbours


def path(node):
    path = []

    while node != None:
        path.append(node)
        node = node.parent

    path.reverse()
    return path


def graph_search(graph, start_node, goal_node):
    frontier = list()
    frontier.append(start_node)
    explored = list()

    while True:
        if frontier == []:
            return False
        leaf = frontier.pop()
        if leaf == goal_node:
            explored.append(leaf)

            print("Path cost:" + str(leaf.path_cost))
            print("")
            exploredString = "["
            for obj in explored:
                exploredString += "(" + str(obj.y) + ", " + str(obj.x) + ")" 
                if(obj.label != "G"):
                        exploredString += ", "
            exploredString += "]"
            print("Explored: " + exploredString)
            print(" ")
            return path(leaf)
        explored.append(leaf)
        for next_node in neighbourhood(graph, leaf):
            curr_path_cost = leaf.path_cost + 1
            if ((next_node not in frontier and next_node not in explored)
                    or (next_node in frontier and curr_path_cost < next_node.path_cost)):
                next_node.parent = leaf
                next_node.path_cost = curr_path_cost
                frontier.append(next_node)
                frontier.sort(key=f_n, reverse=True)
                


def pathfinding(input_filepath):
    # input_filepath contains the full path to a CSV file with the input grid
    graph = list()
    count_x = 0
    count_y = 0

    with open(input_filepath, "r") as inputs:
        tmp = inputs.read().split("\n")
        array = [i.split(",") for i in tmp]
    if([''] in array):
        array.remove([''])

    for row in array:
        for item in row:
            graph.append(node(count_x, count_y, item))
            count_x += 1
        count_y += 1
        count_x = 0

    # convert all tiles adjacent to a hazard to an obstacle
    for obj in graph:
        if(obj.label == "H"):
            hazard_neighbours = neighbourhood(graph, obj)
            for neighbour in hazard_neighbours:
                neighbour.label = "X"
            obj.label = "X"  # also convert the hazard to an obstacle

    for obj in graph:
        if(obj.label == "S"):
            start_node = obj
        elif(obj.label == "G"):
            goal_node = obj

    for obj in graph:
        obj.h = heuristic(obj, goal_node)

    path = graph_search(graph, start_node, goal_node)
    path.reverse()
    pathString ="["
    for obj in path:
        pathString += "(" + str(obj.y) + ", " + str(obj.x) + ")" 
        if(obj.label != "G"):
            pathString += ", "
    pathString += "]"
    print("Path: " + pathString)
    print(" ")

    # optimal_path is a list of tuples indicated the optimal path from start to goal
    # explored_list is the list of nodes explored during search
    # optimal_path_cost is the cost of the optimal path from the start state to the goal state


pathfinding("input.txt")
