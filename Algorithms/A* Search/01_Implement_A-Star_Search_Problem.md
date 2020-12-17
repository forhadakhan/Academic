# Implement the A* Search algorithm for a grid

1. Use the manhattan distance{ (x2-x1)+(y2-y1)} as the h(x) or heuristic value.
1. Use the total number of cell passed till now as g(x) value
1. Print the shortest path beginning at the source and ending at the target node after the algorithm ends. Also print the grid with path and total steps including source.

- Input (maze/grid):  
  Read a file that contains - 
    + A string of dots (.) and hash  (#)
        - .#.#..
        - A dot(.) is a valid path, you can use that cell as your path.
        - A hash(#) is an obstacle you can not pass through that cell so you have to avoid that cell.
    + **s** is the starting point.
    + **t** is the target point.

- Output:
    + Print coordinates (Row, Column)
    + Print the grid with path.
    + Print total steps including source.

*************************

**Input-1:**
```
...#..
.#.#.t
s#....
```

**Output-1:**
```
R,C
---
2,0 (Source)
1,0
0,0
0,1
0,2
1,2
2,2
2,3
2,4
2,5
1,5 (Target)



Path (+) in Grid:

+++#..
+#+#.t
s#++++


Steps to Target: 11

```

-------

**Input-2:**
```
.#.#.###..#t
.#.#...#.##.
...#.#...##.
#.##.#.#.##.
#....#.#....
###.##.#####
s...##......
```

**Output-2:**
```
R,C
---
6,0 (Source)
6,1
6,2
6,3
5,3
4,3
4,4
3,4
2,4
1,4
1,5
1,6
2,6
2,7
2,8
3,8
4,8
4,9
4,10
4,11
3,11
2,11
1,11
0,11 (Target)



Path (+) in Grid:

.#.#.###..#t
.#.#+++#.##+
...#+#+++##+
#.##+#.#+##+
#..++#.#++++
###+##.#####
s+++##......


Steps to Target: 24

```

