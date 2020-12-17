# The main method
def main():
    
    # Get a map (grid)
    map = {}

    chars = ['c']
    source = None
    target = None
    width = 0
    height = 0
    
    # Open a file to read the grid
    file_handle = open('C://Users//forha//Downloads//input.txt', 'r')
    
    # Loop until there is no more lines
    while len(chars) > 0:
        
        # Get chars in a line
        chars = [str(i) for i in file_handle.readline().strip()]
        
        # Calculate the width
        width = len(chars) if width == 0 else width
        
        # Add chars to map
        for x in range(len(chars)):
            map[(x, height)] = chars[x]
            if(chars[x] == 's'):
                source = (x, height)
            elif(chars[x] == 't'):
                target = (x, height)
        
        # Increase the height of the map
        if(len(chars) > 0):
            height += 1
    
    # Close the file pointer
    file_handle.close()
    
    # Find the closest path from source(s) to target(t)
    path = astar_search(map, source, target)
    print()

    # Print coordinates of path
    print("\n")
    print_c(path, map)
    
    # Print the grid with path
    print()
    print_grid(map, width, height, spacing=1, path=path, source=source, target=target)
    
    # Print steps to goal including source and target
    print()
    print('\nSteps to Target: {0}'.format(len(path)))
    print("\n")
# end main()


# Create a class to represent a node
class Node:
    
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to source node
        self.h = 0 # Distance to target node
        self.f = 0 # Total cost
    
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))
# end class Node()


# A* search
def astar_search(map, source, target):
    
    # Create lists for open-nodes and closed-nodes
    open = []
    closed = []
    
    # Create a source node and an target node
    source_node = Node(source, None)
    target_node = Node(target, None)
    
    # Add the source node
    open.append(source_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        
        # Get the node with the lowest cost
        current_node = open.pop(0)
        
        # Add the current node to the closed list
        closed.append(current_node)        
        
        # Check if we have reached the target, return the path
        if current_node == target_node:
            path = []
            while current_node != source_node:
                path.append(current_node.position)
                current_node = current_node.parent
            path.append(source) 
            # Return reversed path
            return path[::-1]
        
        # Unzip the current node position
        (col, row) = current_node.position
        
        # Get neighbors [Left, Right, Up, Down]
        neighbors = [(col-1, row), (col+1, row), (col, row-1), (col, row+1)]
        
        # Loop neighbors
        for next in neighbors:
            
            # Get value from map
            map_value = map.get(next)
            
            # Check if the node is a wall
            if(map_value == '#'):
                continue
            
            # Create a neighbor node
            neighbor = Node(next, current_node)
            
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            
            # Generate heuristics (Manhattan distance)
            neighbor.g = abs(neighbor.position[0] - source_node.position[0]) + abs(neighbor.position[1] - source_node.position[1])
            neighbor.h = abs(neighbor.position[0] - target_node.position[0]) + abs(neighbor.position[1] - target_node.position[1])
            neighbor.f = neighbor.g + neighbor.h
            
            # Check if neighbor is in open-list and if it has a lower f (Total cost) value
            if(add_to_open(open, neighbor) == True):

                # Check if neighbor is valid
                if neighbor.position in map.keys():
                    
                    # Everything is green, add neighbor to open-list
                    open.append(neighbor)
    
    # Return None, no path is found
    return None
# end astar_search()


# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
# end add_to_open()

# Print the grid with path
def print_grid(map, width, height, spacing=2, **kwargs):
    print("\nPath (+) in Grid:\n")
    for y in range(height):
        for x in range(width):
            print('%%-%ds' % spacing % print_tile(map, (x, y), kwargs), end='')
        print()
# end print_grid()


# Print a tile
def print_tile(map, position, kwargs):
    
    # Get the map value
    value = map.get(position)
    # Check if we should print the path
    if 'path' in kwargs and position in kwargs['path']: value = '+'
    # Check if we should print start point
    if 'source' in kwargs and position == kwargs['source']: value = 's'
    # Check if we should print the goal point
    if 'target' in kwargs and position == kwargs['target']: value = 't'
    # Return a tile value
    return value 
# end print_tile()


# Print coordinates of path
def print_c(path, map):
    print("R,C")
    print("---")
    for position in path:
        (col, row) = position
        if map[position] == 's':
            print('{},{} {}'.format(row, col, '(Source)'))
        elif map[position] == 't':
            print('{},{} {}'.format(row, col, '(Target)'))
        else:
            print('{},{}'.format(row, col))
    print()
# end print_c()


# Call main method
if __name__ == "__main__": 
    main()
