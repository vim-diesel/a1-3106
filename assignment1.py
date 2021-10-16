# Name this file to assignment1.py when you submit

class node:
    def __init__(self, x, y, label, parent=None, action=None, path_cost=0):
        self.x = x
        self.y = y
        self.label = label

def pathfinding(input_filepath):
    # input_filepath contains the full path to a CSV file with the input grid
    list = []
    count_x = 0
    count_y = 0
    

    with open(input_filepath, "r") as inputs:
        tmp = inputs.read().split("\n")
        tmp.remove('')
        array = [i.split(",") for i in tmp]

        for row in array:
            for item in row:
                list.append( node(count_x, count_y, item))
                count_x += 1
            count_y += 1
            count_x = 0

        for obj in list:
            print(obj.x, obj.y, obj.label, sep=" ")
            if(obj.label == "S"):
                

    # optimal_path is a list of tuples indicated the optimal path from start to goal
    # explored_list is the list of nodes explored during search
    # optimal_path_cost is the cost of the optimal path from the start state to the goal state
    return 1


pathfinding("input.txt")
