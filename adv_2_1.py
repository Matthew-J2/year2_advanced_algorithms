"""
Defaultdict:
https://realpython.com/python-defaultdict/
sys.maxsize:
https://docs.python.org/3/library/sys.html#sys.maxsize
Typing:
https://docs.python.org/3/library/typing.html
"""

from collections import defaultdict
import sys
from typing import Tuple
from typing import List
from timeit import default_timer as timer


class Graph():
    """
    Graph structure used to implement Dijkstra's algorithm.

    edges(collections.defaultdict): A dictionary containing all nodes as keys and their connections as values.
    weights(dict): A dictionary of all edges between nodes as keys and their weights as values.
    size(int): The number of nodes in the graph.
    dist(int): The distance to a node from the starting node.
    previous(str): A list of the previously visited node for each node.
    """

    def __init__(self, size: int):
        """
        Parameters:
        size(int): The number of nodes in the graph.
        """
        self.edges = defaultdict(list)  # dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}  # dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size
        self.dist = []
        for i in range(size):
            self.dist.append(sys.maxsize)
        self.previous = []
        for i in range(size):
            self.previous.append(None)

    def add_edge(self, from_node: str, to_node: str, weight: int):  # bidirectional
        """
        Adds an edge to the graph

        Parameters:
        from_node(str): The first node of the edge
        to_node(str): The second node of the edge
        weight(int): The weight of the edge
        """
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def findSmallestNode(self):
        """
        Finds the node with smallest distance which is not already in the shortest path

        Finds the distance of the first node in Q.
        Initializes the result as the index of the first node in Q.
        For each item in the list of distances, if the item is smaller than the smallest so far,
        sets current node to the respective node in the unpopped queue.
        If this node is in self.Queue (O(n) operation), set the smallest node to that node's distance,
        and set the result to that node's index.
        Return the result.
        """
        smallest = self.dist[self.getIndex(self.Queue[0])]
        result = self.getIndex(self.Queue[0])
        for i in range(len(self.dist)):
            if self.dist[i] < smallest:
                node = self.unpoppedQueue[i]
                if node in self.Queue:
                    smallest = self.dist[i]
                    result = self.getIndex(node)
        return result

    def getIndex(self, neighbour: str):
        """Performs a linear search (O(n)) to find and return the index of a node"""
        for i in range(len(self.unpoppedQueue)):
            if neighbour == self.unpoppedQueue[i]:
                return i

    def dijkstra(self, start: str, end: str) -> Tuple[List[str], int]:
        """
        Adds each node to the queue.
        Sets distance of start node to 0.
        Makes a copy of self.Queue as unpoppedQueue
        For each node in self.Queue, checks if the smallest adjacent node isn't infinity,
        meaning there is no path to the target, and isn't the target, meaning we can stop
        looking for a path.
        Otherwise, sets the index of the node with smallest distance in the unpopped queue
        as the unpopped node.
        Removes the unpopped node from the queue, and for each adjacent node in the unpopped
        node, find the distance of travelling to the current node to the adjacent one.
        If this distance is less than the current distance to get to the adjacent node,
        set it to be the new distance to travel to the adjacent node, and adds the adjacent node
        to the list of previously visited nodes.
        After the queue of nodes is empty, self.previous is used to backtrack until the starting
        node is found. Each node is inserted (O(n) operation) at the front of the list until
        the shortest path is found.
	https://stackoverflow.com/questions/8537916/how-do-i-prepend-to-a-short-python-list
        """

        self.Queue = []
        for key in self.edges:
            self.Queue.append(key)
        for i in range(len(self.Queue)):
            if self.Queue[i] == start:
                self.dist[i] = 0
        # unpoppedQueue is a copy of self.Queue.
        self.unpoppedQueue = self.Queue[0:]
        while self.Queue:
            u = self.findSmallestNode()
            if self.dist[u] == sys.maxsize:
                break
            if self.unpoppedQueue[u] == end:
                break

            uNode = self.unpoppedQueue[u]

            # remove u from Q
            # for each adjacent vertex v of u
            # alt = distance of u plus cost from u to v
            # if alt is less than the neighbours distance
            # the neighbours distance is alt
            # the previous v is u

            self.Queue.remove(uNode)
            for vNode in self.edges[uNode]:
                alt = self.dist[u] + self.weights[(uNode, vNode)]
                if alt < self.dist[self.getIndex(vNode)]:
                    self.dist[self.getIndex(vNode)] = alt
                    self.previous[self.getIndex(vNode)] = uNode

        shortest_path = []
        shortest_path.insert(0, end)
        u = self.getIndex(end)
        while self.previous[u] != None:
            shortest_path.insert(0, self.previous[u])
            u = self.getIndex(self.previous[u])
        return shortest_path, self.dist[-1]


graph = Graph(8)

edges = [
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
    ('F', 'T', 3),
]

for edge in edges:
    graph.add_edge(*edge)

start = timer()
solution = graph.dijkstra('O', 'T')
end = timer()
print(solution, end - start, sep="\n")

graph2 = Graph(12)

edges2 = [
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
]

for edge in edges2:
    graph2.add_edge(*edge)

start = timer()
solution = graph2.dijkstra('O', 'T')
end = timer()
print(solution, end - start, sep="\n")
