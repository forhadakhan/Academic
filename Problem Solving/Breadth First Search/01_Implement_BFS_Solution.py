#################################################################################
|#|                                                                           |#|
|#|      Problem 01           : Implement Breadth First Search                |#|
|#|                             (Uninformed Search)                           |#|
|#|      Problem (Link)       : http://tiny.cc/2zd6tz                         |#|
|#|      Solution by          : https://github.com/forhadkhan/                |#|
|#|      Python Version       : Python 3.8.5 (Recommended 3.7.+)              |#|
|#|                                                                           |#|
#################################################################################

import queue
from collections import defaultdict 

def main():
    # take input for nodes(n) and edges(m)
    nodes, edges = map(int, input().split())

    # using defualtdict cause it never raises a 'KeyError'
    graph = defaultdict(list)
    
    # taking input for bi-directional edges
    i = 0
    while i < edges:
        i += 1
        a, b = map(int, input().split())
        # Creating the graph as adjacency list
        graph[a].append(b) 
        graph[b].append(a)  
    
    # taking the source(s) node
    source = int(input())

    # Printing the number of edges required at minimum to reach a particular
    # node from the source in a sequence from 0 to nodes-1.
    print("\n\n\nFrom the source ", source, ":\n\n")
    goal = 0
    while goal < nodes:
        if goal != source:
            result = bfs_shortest_path(graph, source, goal)
            if isinstance(result, list):
                min_edges = len(result) - 1
                print("Minimum ", min_edges, " edges needed to reach ", goal)
                print("Path taken: ", end=' ')
                for item in result:
                    print(item, end=' ')
                print()
            else:
                print(result)
        goal += 1
        print()

    # Printing Bonus:
    # all the nodes in which they are explored separated by their levels.
    print("\n\n\nBonus:\n")
    level = bfs_print_levels(graph, nodes, source)
    # sorting level dict by keys
    #levels = {k: level[k] for k in sorted(level)}

    for key, value in sorted(level.items()):
        print('Level ' + str(key) + ': ', end='', )
        print(*value, sep=', ')
    print("\n\n\n")
# end main()


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, source, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    que = [[source]]

    # return path if source is goal
    if source == goal:
        return "Source = Goal"

    # keeps looping until all possible paths have been checked
    while que:
        # pop the first path from the queue
        path = que.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path 
            # and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                que.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case the goal is not reachable.
    output = str(goal) + " is not reachable."
    return output
# end bfs_shortest_path(graph, source, goal)


# function to determine level of each node starting from source
def bfs_print_levels(graph, nodes, source):

    # list/array to store level of each node
    level = [None] * nodes
    visited = [False] * nodes

    # 'source' marked as visited
    visited[source] = True

    # create a queue
    que = queue.Queue()

    # enqueue 'source'
    que.put(source)

    # initialize level of 'source' node to 1
    level[source] = 1

    # do until queue is empty   
    while (not que.empty()):
        # get the first element of queue
        source = que.get()

        # traverse neighbors of node 'source'
        for i in range(len(graph[source])):
            # n is neighbor of node 'source'
            n = graph[source][i]

            # if n is not visited yet
            if (not visited[n]):
                # enqueue n in queue
                que.put(n)
                # mark n as visited
                visited[n] = True

                # level of n is level of 'source + 1'
                level[n] = level[source] + 1

    # return nodes explored per level
    explored_per_level = dict()
    for i in range(nodes):
        l = level[i]
        if l is not None:
            if l not in explored_per_level:
                explored_per_level[l] = []
            explored_per_level[l].append(i)
    return explored_per_level
# end bfs_print_levels(graph, nodes, source)


# Call the main function:
if __name__ == "__main__":
    main()
