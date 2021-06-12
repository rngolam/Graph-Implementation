# Graphs

An implementation of Undirected and Directed Graph data structures written in Python.

The Directed Graph class is implemented using a vertex adjacency matrix and supports the following interface:
* add_vertex
* add_edge
* remove_edge
* get_vertices
* get_edges
* is_valid_path
* dfs (performs a depth-first search from a given starting vertex)
* bfs (performs a breadth-first search traversal from a given starting vertex)
* has_cycle
* dijkstra (returns a list of the shortest path to all vertices using Dijkstra's Algorithm)

Example Input:
```python
edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
         (3, 1, 5), (2, 1, 23), (3, 2, 7)]
g = DirectedGraph(edges)
for i in range(5):
    print(f'DIJKSTRA {i} {g.dijkstra(i)}')
g.remove_edge(4, 3)
print('\n', g)
for i in range(5):
    print(f'DIJKSTRA {i} {g.dijkstra(i)}')
```
![image](https://user-images.githubusercontent.com/69094063/121775107-42490700-cb4b-11eb-909f-c27c1c89e703.png)

Output:
```
dijkstra() example 1
--------------------------
DIJKSTRA 0 [0, 10, 35, 28, 25]
DIJKSTRA 1 [27, 0, 25, 18, 15]
DIJKSTRA 2 [50, 23, 0, 41, 38]
DIJKSTRA 3 [32, 5, 7, 0, 20]
DIJKSTRA 4 [12, 8, 10, 3, 0]

 GRAPH (5 vertices):
   | 0  1  2  3  4
------------------
 0 | 0 10  0  0  0
 1 | 0  0  0  0 15
 2 | 0 23  0  0  0
 3 | 0  5  7  0  0
 4 |12  0  0  0  0

DIJKSTRA 0 [0, 10, inf, inf, 25]
DIJKSTRA 1 [27, 0, inf, inf, 15]
DIJKSTRA 2 [50, 23, 0, inf, 38]
DIJKSTRA 3 [32, 5, 7, 0, 20]
DIJKSTRA 4 [12, 22, inf, inf, 0]
```

The Undirected Graph class is implemented using a vertex adjacency list and supports the following interface:
* add_vertex
* add_edge
* remove_edge
* get_vertices
* get_edges
* is_valid_path
* dfs (performs a depth-first search traversal from a given starting vertex)
* bfs (performs a breadth-first search traversal from a given starting vertex)
* count_connected_components
* has_cycle

Example Input:
```python
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')
```
Output:
```
method dfs() and bfs() example 1
--------------------------------------
A DFS:['A', 'C', 'B', 'D', 'E', 'H'] BFS:['A', 'C', 'E', 'B', 'D', 'H']
B DFS:['B', 'C', 'A', 'E', 'D', 'H'] BFS:['B', 'C', 'D', 'E', 'H', 'A']
C DFS:['C', 'A', 'E', 'B', 'D', 'H'] BFS:['C', 'A', 'B', 'D', 'E', 'H']
D DFS:['D', 'B', 'C', 'A', 'E', 'H'] BFS:['D', 'B', 'C', 'E', 'H', 'A']
E DFS:['E', 'A', 'C', 'B', 'D', 'H'] BFS:['E', 'A', 'B', 'C', 'D', 'H']
G DFS:['G', 'F', 'Q'] BFS:['G', 'F', 'Q']
H DFS:['H', 'B', 'C', 'A', 'E', 'D'] BFS:['H', 'B', 'C', 'D', 'E', 'A']
-----
B-G DFS:['B', 'C', 'A', 'E', 'D', 'H'] BFS:['B', 'C', 'D', 'E', 'H', 'A']
C-E DFS:['C', 'A', 'E'] BFS:['C', 'A', 'B', 'D', 'E']
D-D DFS:['D'] BFS:['D']
E-C DFS:['E', 'A', 'C'] BFS:['E', 'A', 'B', 'C']
G-B DFS:['G', 'F', 'Q'] BFS:['G', 'F', 'Q']
H-A DFS:['H', 'B', 'C', 'A'] BFS:['H', 'B', 'C', 'D', 'E', 'A']
```
