# Course: CS261 - Data Structures
# Author: Richard Ngo-Lam
# Assignment: 6
# Description: Implements an UndirectedGraph class.

import heapq
from collections import deque

class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        if v in self.adj_list:
            return
        
        self.adj_list[v] = []


    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if u == v:
            return

        if u not in self.adj_list:
            self.add_vertex(u)

        if v not in self.adj_list:
            self.add_vertex(v)

        if v in self.adj_list[u]:
            return

        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        if u not in self.adj_list or v not in self.adj_list:
            return

        # Attempt to remove edge from adjacency lists if it exists
        try:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)
        except ValueError:
            return
        

    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v not in self.adj_list:
            return

        # Remove all edges connected to parameterized vertex
        for vertex in self.adj_list:
            self.remove_edge(v, vertex)
        
        # Remove parameterized vertex from adjacency lists
        del self.adj_list[v]


    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        res = []
        
        for vertex in self.adj_list:
            res.append(vertex)

        return res
       

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        res = set()

        for vertex_1 in self.adj_list:

            for vertex_2 in self.adj_list[vertex_1]:

                # Check whether permutation of vertices was already accounted for
                if (vertex_2, vertex_1) not in res:
                    res.add((vertex_1, vertex_2))
        
        return list(res)

        
    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """

        last_visited = None

        for vertex in path:

            if vertex not in self.adj_list:
                return False

            # Check if edge exists from last visited vertex to current vertex
            if last_visited and vertex not in self.adj_list[last_visited]:
                return False

            # Update last visited vertex
            last_visited = vertex

        return True
       

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        path = []

        if v_start not in self.adj_list:
            return path

        # Use a stack ADT to store neighboring vertices
        stack = deque()
        visited = set()

        stack.append(v_start)

        while len(stack) > 0:

            current = stack.pop()

            if current == v_end:
                path.append(current)
                break

            if current not in visited:
                visited.add(current)
                path.append(current)

                # Sort adjacency list in reverse-lexicographical order so that
                # vertices at the beginning of the alphabet are at the top of
                # the stack
                self.adj_list[current].sort(reverse=True)

                for vertex in self.adj_list[current]:
                    stack.append(vertex)

        return path


    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        path = []

        if v_start not in self.adj_list:
            return path

        # Use a queue ADT to store neighboring vertices
        queue = deque()
        visited = set()

        queue.append(v_start)

        while len(queue) > 0:

            current = queue.popleft()

            if current == v_end:
                path.append(current)
                break

            if current not in visited:
                visited.add(current)
                path.append(current)

                self.adj_list[current].sort()

                for vertex in self.adj_list[current]:
                    queue.append(vertex)

        return path
        

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        vertices = set(self.adj_list.keys())

        connected_count = 0

        while len(vertices) > 0:
            
            vertex = vertices.pop()

            # Perform DFS to return a set of all components connected to
            # a given vertex
            connected = set(self.dfs(vertex))
            
            # Remove the connected components from the set of unvisited vertices
            vertices -= connected
            connected_count += 1

        return connected_count


    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        unvisited = {vertex for vertex in self.adj_list}
        visited = set()

        # Test every unvisited vertex
        while len(unvisited) > 0:

            vertex = unvisited.pop()

            if self.has_cycle_rec(vertex, unvisited, visited):
                return True
        
        return False


    def has_cycle_rec(self, vertex, unvisited, visited, last_visited=None):
        """
        Recursive helper method for has_cycle
        """
        # Move vertex from set of unvisited to visited vertices
        unvisited.discard(vertex)
        visited.add(vertex)

        for neighbor in self.adj_list[vertex]:
            
            # Base case: If the neighboring vertex has already been visited and
            # it is not the parent vertex, then there is a cycle
            if neighbor in visited and neighbor != last_visited:
                return True

            # Recursive case: check whether there is a cycle at the neighboring
            # vertex
            if neighbor not in visited:
                if self.has_cycle_rec(neighbor, unvisited, visited, vertex):
                    return True

        # Base case: If vertex has no neighbors to process, there is no cycle
        return False


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
