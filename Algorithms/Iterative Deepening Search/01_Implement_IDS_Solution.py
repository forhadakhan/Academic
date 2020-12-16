
from collections import defaultdict 

def main():

    #taking input for nodes (n) and edges (m)
    nodes, edges = map(int, input().split())

    # initializing a graph for adjacncy list
    graph = defaultdict(list)
    
    # taking input for bi-directional edges
    for i in range(edges):
        a, b = map(int, input().split())
        graph[a].append(b) 
        graph[b].append(a)  
    
    # taking source
    source = int(input())
    
    # The highest depth limit
    max_limit = 9 + 1
    print("\n")
    
    # iterating upto highest depth limit
    for max_depth in range(max_limit):

        print("\nWhen depth limit: ", max_depth, "\n")
        
        visited = [0]*nodes
        depth = [0]*nodes
        
        ids(graph, source, visited, depth, max_depth)
    
    print("\n\n\n")
# end main()


def ids(graph, source, visited, depth, max_depth):
    
    # Mark source as visited
    visited[source] = 1
    
    print("Explored", source, "at depth", depth[source])
    
    # Iterate through the neighbour of current source
    for neighbour in graph[source]:
        
        # if neighbour isn't visited yet
        if visited[neighbour] == 0:
            
            # increase depth
            depth[neighbour] = depth[source]+1
            
            # if neighbours depth excess the max depth limit then continue
            if depth[neighbour] > max_depth:
                continue
            # else do recursion
            else:
                ids(graph, neighbour, visited, depth, max_depth)
# end ids(graph, source, visited, depth, max_depth)


# Call the main function:
if __name__ == "__main__":
    main()
