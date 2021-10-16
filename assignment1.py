# Name this file to assignment1.py when you submit
#from pathlib import Path

#data_folder = Path("/home/ubuntu/3106/a1")

#input_file = data_folder / "input.txt"


def pathfinding(input_filepath):
    # input_filepath contains the full path to a CSV file with the input grid
    with open(input_filepath, "r") as inputs:
        
        tmp = inputs.read().split("\n")
        tmp.remove('')
        array = [i.split(",") for i in tmp]
        for row in array:
          for item in row:
            print(item, end=" ")
          print("")

            
        
    # optimal_path is a list of tuples indicated the optimal path from start to goal
    # explored_list is the list of nodes explored during search
    # optimal_path_cost is the cost of the optimal path from the start state to the goal state
    return 1


pathfinding("input.txt")
