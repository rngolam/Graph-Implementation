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
