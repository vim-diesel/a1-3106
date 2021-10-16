# Name this file to assignment1.py when you submit

class node:
    def __init__(self, x, y, label, parent=None, action=None, path_cost=0, h=0):
        self.x = x
        self.y = y
        self.label = label

def heuristic(curr_node, goal_node):
    D = 1 #simple move cost of 1
    dx = abs(curr_node.x - goal_node.x)
    dy = abs(curr_node.y - goal_node.y)
    return D * (dx + dy)

def pathfinding(input_filepath):
    # input_filepath contains the full path to a CSV file with the input grid
    list = []
    count_x = 0
    count_y = 0
    frontier = []
    explored = []
    

    with open(input_filepath, "r") as inputs:
        tmp = inputs.read().split("\n")
        tmp.remove('')
        array = [i.split(",") for i in tmp]
    
    
    for row in array:
        for item in row:
            list.append(node(count_x, count_y, item))
            count_x += 1
        count_y += 1
        count_x = 0
    for obj in list:
        if(obj.label == "S"):
            start_node = obj
        elif(obj.label == "G"):
            goal_node = obj
    for obj in list:
        obj.h = heuristic(obj, goal_node)
    for obj in list:
        if (obj == "S"):
            start_node = obj
            frontier.append(start_node)
    
    

    

            
    for obj in list:
        print(obj.x, obj.y, obj.label, obj.h, sep=" ")
            
    # optimal_path is a list of tuples indicated the optimal path from start to goal
    # explored_list is the list of nodes explored during search
    # optimal_path_cost is the cost of the optimal path from the start state to the goal state
    return 1


pathfinding("input.txt")
