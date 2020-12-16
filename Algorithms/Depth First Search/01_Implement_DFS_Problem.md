##  Implement Depth First Search (Uninformed Search)

1.  You are given an undirected or bidirected graph and a source from which you will start your journey 
    You have to find and print the list of vertices you can go from the source vertice given as input.  
    + First will have the total number of nodes **(n)**  and the total number of edges **(m)**.    
    + Next m lines will be followed by m pairs of integers denoting the bi-directional edges.  
        - **a   b**  
            + It means there is a connection from **a to b** and 
            + Also, a connection from **b to a**.
    + Then a single integer **s** denoting the source.  
1.  Use the idea of Graph traversal to solve the problem. Also use **recursive** method.  

1.  Outputs:  
    + Print the nodes in the order they are getting explored starting from the source node including in which depth level they were explored.  
    + Maximum depth Reached for the corresponding DFS.  
1.  Use the idea of Graph traversal to solve the problem.  


**Input-1:**  
```
14 12
0 1
0 4
0 2
1 3
1 4
3 5
5 6
5 7
6 8
2 11
11 10
9 13
0

```

**Output-1:**  
```
Explored  0 at depth 0
Explored  1 at depth 1
Explored  3 at depth 2
Explored  5 at depth 3
Explored  6 at depth 4
Explored  8 at depth 5
Explored  7 at depth 4
Explored  4 at depth 2
Explored  2 at depth 1
Explored  11 at depth 2
Explored  10 at depth 3
  
Maximum Depth reached: 5
  
```
  
  
**Input-2:**  
```
14 10
0 1
0 2
0 4
1 3
1 4
2 11
3 5
6 7
8 9
10 13
4

```
**Output-2:**  
```
Explored  4 at depth 0
Explored  0 at depth 1
Explored  1 at depth 2
Explored  3 at depth 3
Explored  5 at depth 4
Explored  2 at depth 2
Explored  11 at depth 3

Maximum Depth reached: 4
  
```
  
  
**Input-3:**  
```
7 5
1 2
1 4
2 5
3 6
0 6
6

```
**Output-3:**
```
Explored  6 at depth 0
Explored  3 at depth 1
Explored  0 at depth 1
  
Maximum Depth reached: 1
  
```
