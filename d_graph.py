# Course: CS261 - Data Structures
# Author: Richard Ngo-Lam
# Assignment: 6
# Description: Implements a DirectedGraph class.

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        TODO: Write this implementation
        """

        # Add row
        self.adj_matrix.append([0] * (self.v_count + 1))
        
        # Add columns to existing rows, excluding row that was just added
        for i in range(self.v_count):
            self.adj_matrix[i].append(0)

        self.v_count += 1

        return self.v_count
        

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        TODO: Write this implementation
        """
        # Vertex indices not in graph
        if src < 0 or dst < 0 or src > len(self.adj_matrix) - 1 or dst > len(self.adj_matrix) - 1:
            return

        # Source and destination refer to the same vertex
        if src == dst:
            return

        # Weight is not a positive integer
        if weight < 1:
            return

        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        TODO: Write this implementation
        """
        # Vertex indices not in graph
        if src < 0 or dst < 0 or src > len(self.adj_matrix) - 1 or dst > len(self.adj_matrix) - 1:
            return

        self.adj_matrix[src][dst] = 0


    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        return [x for x in range(len(self.adj_matrix))]

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        res = []

        for i in range(len(self.adj_matrix)):

            for j in range(len(self.adj_matrix[i])):

                if self.adj_matrix[i][j] != 0:

                    res.append((i, j, self.adj_matrix[i][j]))

        return res


    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        # Empty paths are valid
        if len(path) == 0:
            return True
        
        for i in range(len(path) - 1):

            if self.adj_matrix[path[i]][path[i + 1]] == 0:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        visited = set()
        path = []

        stack = deque()
        stack.append(v_start)

        while len(stack) > 0:

            current = stack.pop()

            if current == v_end:
                path.append(current)
                break

            if current not in visited:

                visited.add(current)
                path.append(current)

                # Push vertices to stack in descending order so that lower indices
                # are at the top and will be visited first
                for i in range(len(self.adj_matrix) - 1, -1, -1):

                    if self.adj_matrix[current][i] != 0:
                        stack.append(i)

        return path

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        visited = set()
        path = []

        queue = deque()
        queue.append(v_start)

        while len(queue) > 0:

            current = queue.popleft()

            if current == v_end:
                path.append(current)
                break

            if current not in visited:

                visited.add(current)
                path.append(current)

                for i in range(len(self.adj_matrix)):

                    if self.adj_matrix[current][i] != 0:
                        queue.append(i)

        return path

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        for i in range(len(self.adj_matrix)):

            if self.has_cycle_rec(i):
                return True

        return False

    
    def has_cycle_rec(self, vertex, last_visited=None, visited=None):
        """
        """
        if visited is None:
            visited = set()

        # We can't consider a vertex visited until we finish fully processing it
        if last_visited:
            visited.add(last_visited)

        for successor in range(len(self.adj_matrix[vertex])):

            if self.adj_matrix[vertex][successor] != 0:

                if successor in visited and successor != last_visited:
                    return True

                if successor not in visited:
                    if self.has_cycle_rec(successor, vertex, visited):
                        return True

        return False


    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        visited = dict()
        priority_queue = []
        
        heapq.heappush(priority_queue, (0, src))

        while len(priority_queue) > 0:

            # Represents distance to the current vertex
            distance, current = heapq.heappop(priority_queue)

            if current not in visited:
                
                visited[current] = distance

                # Insert each neighbor and its associated distance into
                # MinHeap/priority queue, where the closest neighbor is at the
                # front of the queue
                for neighbor in range(len(self.adj_matrix[current])):

                    if self.adj_matrix[current][neighbor] != 0:

                        heapq.heappush(priority_queue, (distance + self.adj_matrix[current][neighbor], neighbor))

        res = [float('inf')] * len(self.adj_matrix)

        for vertex in visited:

            res[int(vertex)] = visited[vertex]

        return res



if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = DirectedGraph()
    print(g)
    for _ in range(5):
        g.add_vertex()
    print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
    print(g)


    print("\nPDF - method get_edges() example 1")
    print("----------------------------------")
    g = DirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for start in range(5):
        print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
