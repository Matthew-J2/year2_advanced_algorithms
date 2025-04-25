"""
Typing documentation:
https://docs.python.org/3/library/typing.html
sys.maxsize documentation:
https://docs.python.org/3/library/sys.html#sys.maxsize
__slots__ use case:
https://wiki.python.org/moin/UsingSlots
Append to beginning of list:
https://stackoverflow.com/questions/17911091/append-integer-to-beginning-of-list-in-python
List information:
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
Deque:
https://docs.python.org/3/library/collections.html#collections.deque
Time complexity of structures:
https://wiki.python.org/moin/TimeComplexity
Priority Queue:
https://www.geeksforgeeks.org/priority-queue-in-python/
https://likegeeks.com/python-priority-queue/
Priority Queue using heapdict:
https://www.geeksforgeeks.org/priority-queue-in-python/
Heapdict download and source code:
https://pypi.org/project/HeapDict/
Min-heap information:
https://www.educative.io/answers/min-heap-vs-max-heap
Dijkstra's algorithm explanation:
https://www.youtube.com/watch?v=GazC3A4OQTE
"""

import sys
import heapdict
from collections import deque
from typing import Tuple
from typing import List
from timeit import default_timer as timer


class Graph:
    """
    Class representing the graph Dijkstra's algorithm is to be performed on.

    nodes(list): A list containing the name of each node.
    edges(dict{dict}): A nested dictionary representing the edges of each node. The outer node's
    name is stored as the outer key. The value for the key is another dictionary. For each inner
    dictionary, the key stores the other node forming the edge, and the inner value stores the weight
    of the edge.
    size(int): The number of nodes in the graph.
    """
    __slots__ = ('nodes', 'edges', 'size')

    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.size = 0

    def add_node(self, node: str):
        """
        Adds a node to the list of nodes and increases the graph's size.

        Parameters:
        node (str): The node to be added.
        """
        self.nodes.append(node)
        self.edges[node] = {}
        self.size += 1

    def add_edge(self, node: str, edge: str, weight: int):
        """
        Adds an edge to the graph.

        Parameters:
        node (str): The node the edge starts from.
        edge (str): The node the edge links to.
        weight (int): The value of the edge.
        """
        if node == edge:
            self.edges[node][node] = 0
        self.edges[node][edge] = weight
        self.edges[edge][node] = weight

    def dijkstra(self, start: str, target: str) -> Tuple[List[str], int]:
        """
        Performs dijkstra's algorithm on a the graph, given a starting and target node.

        Parameters:
        start (str): The name of the starting node.
        target (str): The name of the target node.

        Returns:
        list: Stores each vertex to represent the lowest order of traversal.
        int: The total cost of the shortest path.
        """
        # visited_nodes is a list of the previous nodes checked
        visited_nodes = [None] * self.size

        # distances is a dictionary containing the node as a key and its current smallest distance as a value
        distances = {}

        # node_idx_dict is a dictionary used for O(1) index lookup for a node as opposed to using in or index() on a
        # list, both of which are O(n).
        node_idx_dict = {}

        # Priority queue structure used to check the nodes with the smallest values first, reducing overall time
        # complexity from O(n^2) to O(Elog(V)).
        priority_queue = heapdict.heapdict()

        # Sets distances and priority queue values. The starting node's distance is 0, and the others are the maximum
        # integer size, as this is the next best thing to infinity.
        for idx, node in enumerate(self.nodes):
            node_idx_dict[node] = idx
            if node == start:
                priority_queue[start] = 0
                distances[node] = 0
            else:
                priority_queue[node] = sys.maxsize
                distances[node] = sys.maxsize
        # Loops for each item in the priority queue.
        while priority_queue:

            # Pop the node with smallest distance from the queue. If the distance is sys.maxsize, the
            # node can't be reached, If the smallest node is the target, we have a solution.
            current_node, current_value = priority_queue.popitem()
            if current_value == sys.maxsize:
                break
            if current_node == target:
                break

            # Finds the distance of the current node added to its neighbour (found by self.find_smallest()), and checks
            # if it is smaller than the existing distance for that node. If so, it replaces the old distance, and
            # updates the distances dictionary, priority queue values, and the list of visited nodes.
            for edge in self.edges[current_node]:
                if edge == start or not edge in priority_queue:
                    continue
                alt_distance = current_value + self.edges[current_node][edge]
                if alt_distance < distances[edge]:
                    distances[edge] = alt_distance
                    priority_queue[edge] = alt_distance
                    visited_nodes[node_idx_dict[edge]] = current_node

        # Constructs the solution by inserting nodes into the left of a doubly ended queue. This is an O(1) operation
        # as opposed to in a list, where this would be O(n) for every insert.

        # Loops over visited_nodes to add each non duplicated element to the deque until the starting node is found.
        # A set is used to check if there are any duplicates in O(1) time. A set cannot be used directly as sets are
        # unordered.
        shortest_path = deque()
        shortest_path.appendleft(target)
        current_backtracked_node = visited_nodes[node_idx_dict[target]]
        for node in range(self.size):
            if current_backtracked_node is None:
                break
            shortest_path.appendleft(current_backtracked_node)
            current_backtracked_node = visited_nodes[node_idx_dict[current_backtracked_node]]
        return list(shortest_path), distances[target]


def main():
    g = Graph()
    nodes = ["O", "A", "B", "C", "D", "F", "E", "T"]
    [g.add_node(i) for i in nodes]

    edges = (
        ('O', 'A', 2),
        ('O', 'B', 5),
        ('O', 'C', 4),
        ('A', 'B', 2),
        ('A', 'D', 7),
        ('A', 'F', 12),
        ('B', 'C', 1),
        ('B', 'D', 4),
        ('B', 'E', 3),
        ('C', 'E', 4),
        ('D', 'E', 1),
        ('D', 'T', 5),
        ('E', 'T', 7),
        ('F', 'T', 3)
    )
    [g.add_edge(i[0], i[1], i[2]) for i in edges]
    start = timer()
    solution = g.dijkstra("O", "T")
    end = timer()
    print(solution, end - start, sep="\n")

    g2 = Graph()
    nodes = ["O", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "T"]
    [g2.add_node(i) for i in nodes]
    edges = (
        ("O", "A", 6),
        ("O", "B", 8),
        ("A", "B", 2),
        ("A", "C", 5),
        ("B", "D", 2),
        ("A", "E", 14),
        ("D", "E", 3),
        ("D", "F", 4),
        ("C", "G", 7),
        ("E", "H", 2),
        ("G", "H", 4),
        ("F", "I", 3),
        ("I", "H", 8),
        ("H", "J", 7),
        ("J", "T", 1),
        ("H", "T", 10),
        ("I", "T", 11)
    )
    [g2.add_edge(i[0], i[1], i[2]) for i in edges]
    start = timer()
    solution = g2.dijkstra("O", "T")
    end = timer()
    print(solution, end - start, sep="\n")


if __name__ == "__main__":
    main()
