#################################################################################
##|                                                                           |##
##|      Problem 01           : Implement Depth First Search                  |##
##|                             (Uninformed Search)                           |##
##|      Solution by          : https://github.com/forhadkhan/                |##
##|      Python Version       : Python 3.8.5 (Recommended 3.7.+)              |##
##|                                                                           |##
#################################################################################

from collections import defaultdict 

def main():

    #taking inputs for nodes (n) and edges (m)
    nodes, edges = map(int, input().split())

    # initializing a graph for adjacncy list
    graph = defaultdict(list)
    
    # taking inputs for bi-directional edges
    i = 0
    while i < edges:
        i += 1
        a, b = map(int, input().split())
        graph[a].append(b) 
        graph[b].append(a)  
    
    # taking source/stating node
    source = int(input())
    print("\n")
    
    # calling dfs recursive function
    path = recursive_dfs(graph, source, 0)

    print("\nMaximum Depth reached:", path[0], "\n\n")
# end main()


# dfs recursive function
# path[0] initialized with string "0" (as our main path is int)
# for counting maximum depth
def recursive_dfs(graph, source, depth, path = ["0"]):      

    if source not in path:        
        # adding a newly explored node in the path as visited
        path.append(source)
        print("Explored", source, "at depth", depth)

        # upadating maximum depth
        if path[0] < str(depth):
            path[0] = str(depth)
        depth += 1        

        # leaf node, backtrack
        if source not in graph:            
            return path

        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, depth, path)
        # decrease depth in case of backtrack
        depth -= 1
    return path
# end recursive_dfs(graph, neighbour, depth, path)


# Call the main function:
if __name__ == "__main__":
    main()

