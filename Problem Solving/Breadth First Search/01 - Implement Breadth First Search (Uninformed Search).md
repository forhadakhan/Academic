# Implement Breadth First Search (Uninformed Search)



1. You are given an undirected or bi-directed graph and a source from which you will start your journey. You have to find the minimum number of edges required to arrive at each of the reachable vertices and print the path as given in the output section in a sequence.
    + First will have the total number of nodes **(n)** and the total number of edges **(m)**.
        + Nodes are numbered from **0** to **n-1**
    + Next m lines will be followed by m pairs of integers denoting the bi-directional edges.
        2. a   b
            1. It means there is a connection from **a to b** and 
            2. Also, a connection from **b to a**.
    + Then a single integer **s** denoting the source node.
 
2. Outputs:
    - Print the number of edges required at minimum to reach a particular node from the source in a sequence from 0 to n-1.
    - Avoid printing the distance for the source node.
    - If a node is not reachable. Mention that.
    - See the output format for more details.

3. Bonus Output: 
    + Print all the nodes in which they are explored separated by their levels.
    + This one not shown in the output section below.
    + For the first output, It should be like:


    ```
        Level 1:  0  
        Level 2:  1, 4, 2  
        Level 3:  3, 11   
        Level 4:  5, 10   
        Level 5:  6, 7  
        Level 6:  8  
    ```

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
From the source 0 : 

Minimum   1  edges needed to reach   1
Path taken:   0 1 

Minimum   1  edges needed to reach   2
Path taken:   0 2 

Minimum   2  edges needed to reach   3
Path taken:   0 1 3 

Minimum   1  edges needed to reach   4
Path taken:   0 4 

Minimum   3  edges needed to reach   5
Path taken:   0 1 3 5 

Minimum   4  edges needed to reach   6
Path taken:   0 1 3 5 6 

Minimum   4  edges needed to reach   7
Path taken:   0 1 3 5 7 

Minimum   5  edges needed to reach   8
Path taken:   0 1 3 5 6 8 

9 is not reachable.

Minimum   3  edges needed to reach   10
Path taken:   0 2 11 10 

Minimum   2  edges needed to reach   11
Path taken:   0 2 11 

12 is not reachable.

13 is not reachable.


Bonus:

Level 1:  0
Level 2:  1, 4, 2, 
Level 3:  3, 11 
Level 4:  5, 10 
Level 5:  6, 7
Level 6:  8
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
**Outout-2:**

```
From the source 4 : 

Minimum   1  edges needed to reach   0
Path taken:   4 0 

Minimum   1  edges needed to reach   1
Path taken:   4 1 

Minimum   2  edges needed to reach   2
Path taken:   4 0 2 

Minimum   2  edges needed to reach   3
Path taken:   4 1 3 

Minimum   3  edges needed to reach   5
Path taken:   4 1 3 5 

6 is not reachable.

7 is not reachable.

8 is not reachable.

9 is not reachable.

10 is not reachable.

Minimum   3  edges needed to reach   11
Path taken:   4 0 2 11 

12 is not reachable.

13 is not reachable.


Bonus:

Level 1:  4
Level 2:  0, 1 
Level 3:  2. 3 
Level 4:  5, 11 
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
From the source 6 : 

Minimum   1  edges needed to reach   0
Path taken:   6 0 

1 is not reachable.

2 is not reachable.

Minimum   1  edges needed to reach   3
Path taken:   6 3 

4 is not reachable.

5 is not reachable.


Bonus:

Level 1:  6
Level 2:  0, 3
```
