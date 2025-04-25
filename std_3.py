"""
Magic methods:
https://dbader.org/blog/python-dunder-methods
__str__ and __repr__, print() implementation:
https://realpython.com/python-print/
"""


class Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def __str__(self):
        """
        Pretty prints adjacency matrix with margins for rows and columns.
        Creates string representing the matrix and adds margins with add_sides()
        String is created by joining each value in the row with the correct number of spaces,
        then joining each row with a newline.

        Returns:
        str: The completed adjacency matrix string, with the sides appended.
        """

        spaces = len(str((self.size) - 1)) + 1
        adj_matrix_str = '\n'.join(
            (" " * spaces).join(str(value) for value in row
                                ) for row in self.adjMatrix)

        return self._add_sides(adj_matrix_str, spaces)

    def _add_sides(self, adj_matrix_str, spaces):
        """
        Adds the sides of the pretty printed string.

        Parameters:
        adj_matrix_str(str): The string representing the adjacency matrix
        spaces(int): The number of extra spaces required between each column

        Returns:
        str: The completed adjacency matrix string, with the sides appended.
        """

        # Adds a new line with the correct amount of whitespace at the beginning of the string
        adj_matrix_str = " " * (len(str(self.size))) + "\n" + adj_matrix_str

        # Adds the whitespace betweem the column of numbers and the line, and adds the vertical columns,
        # line, and numbers.
        adj_matrix_str = adj_matrix_str.replace("\n", "\nx | ")
        for i in range(self.size):
            adj_matrix_str = adj_matrix_str.replace("x", f"{i + 1}" + " " * (spaces - len(str(i + 1))), 1)

        # Adds the horizontal line.
        adj_matrix_str = "\n" + " " * (1 + spaces) + "-" * ((1 + spaces) * self.size) + adj_matrix_str

        # Adds the horizontal row of numbers.
        for i in range(self.size, 0, -1):
            adj_matrix_str = str(i) + " " * (spaces - len(str(i)) + 1) + adj_matrix_str

        # Adds the whitespace at the beginning of the string.
        adj_matrix_str = " " * (spaces + 3) + adj_matrix_str

        return adj_matrix_str

    def add_vertex(self, edges=None):
        """
        Adds a vertex, which defaults to having 0 edges.
        Adds another row and column to the adjacency matrix.
        Calls add_edges to add any edges to the graph.

        Parameters:
        edges(iterator): A structure containing the other vertices the new vertex will connect to.
        """
        self.size += 1
        for i in self.adjMatrix:
            i.append(0)
        self.adjMatrix.append([0 for i in range(self.size)])
        if edges:
            self.add_edges(self.size - 1, edges)

    def add_edges(self, vertex, edges):
        """
        Calls add_edge() on multiple edges.

        Parameters:
        vertex(int): The index of the vertex to be added to.
        edges(iterator): A structure containing the other vertices the edges will connect to.
        """
        for i in edges:
            self.add_edge(vertex, i)

    def add_edge(self, vertex, edge):
        """
        Sets both the co-ordinates of the edge to 1
        to represent itself in the matrix. If the edge
        connects to itself, sets to 2.

        Parameters:
        vertex(int): The index of the edge to be added to.
        edge(int): The index of the other vertex used to form an edge.
        """

        if vertex != edge:
            self.adjMatrix[vertex][edge] = 1
            self.adjMatrix[edge][vertex] = 1
        else:
            self.adjMatrix[vertex][vertex] = 2

    def remove_vertex(self, vertex):
        """
        Removes the row and column corresponding to vertex.
        Reduces the size of the matrix to represent the vertex being removed.

        Parameters:
        vertex(int): The index of the vertex to be removed.
        """
        self.size -= 1
        del self.adjMatrix[vertex]
        for i in self.adjMatrix:
            del i[vertex]

    def remove_edge(self, vertex, edge):
        """
        Sets the adjacency matrix values representing the edge to 0.

        Parameters:
        vertex(int): The index of the edge to be removed.
        edge(int): The index of the other vertex used to form the edge to be removed.
        """
        self.adjMatrix[vertex][edge] = 0
        self.adjMatrix[edge][vertex] = 0

def main():
    g = Graph(9)
    g.add_edges(2, (4, 5, 2))
    g.add_edges(2, (7,))
    g.add_edges(3, (4, 6))
    print("Graph of size 9, with edges (2,4), (2,5), (2,2), (2,7), (3,4), (3,6)")
    print(g)
    g.remove_vertex(2)
    print("Vertex 2 removed.")
    print(g)
    g.remove_edge(2, 5)
    print("Remove edge (2,5)")
    print(g)
    g.add_vertex((4,))
    g.add_vertex((4, 6, 2, 8))
    print("Add vertex with edges to 4, 5, 2, and 8.")
    print(g)
    g.add_vertex()
    print("Add a vertex with no edges.")
    print(g)


if __name__ == '__main__':
    main()
