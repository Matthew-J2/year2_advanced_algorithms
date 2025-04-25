import sys  # needed for maxsize


class Graph():

    def __init__(self, vertices):  # implements graph as adjacency matrix
        self.V_num = vertices  # number of vertices
        self.graph = [[0 for column in range(vertices)]  # adjacency matrix with no edges (all connections set to zero)
                      for row in range(vertices)]

    def printMST(self, mst_edges):
        print("Edge \t Weight")
        print(mst_edges)
        for vertex in range(1, self.V_num):
            print(mst_edges[vertex], "-", vertex, "\t",
                  self.graph[vertex][mst_edges[vertex]])

            # from reached nodes find the unreached node with the minimum cost

    def minKey(self, key, mstSet):
        """Finds minimum edge from a key"""
        min = sys.maxsize  # set min to infinity (use maxsize which is next best thing!)
        for v_idx in range(self.V_num):  # count through number of vertices
            if key[v_idx] < min and mstSet[v_idx] == False:  # if vertex is less than min and unreached
                min = key[v_idx]  # assign to min
                min_index = v_idx  # min_index is position of min in key
        return min_index  # return min_index

        # find MST

    def primMST(self):
        key = [sys.maxsize] * self.V_num  # initialise key to list of values all set to infinity; same length as self.V
        mst_edges = [None] * self.V_num  # list for constructed MST
        key[0] = 0  # set first element of key to zero (this is where we start)
        mstSet = [False] * self.V_num  # mstSet is list of booleans set to False
        mst_edges[0] = -1  # first element of mst_edges list set to -1

        for vertex in range(self.V_num):  # go through all vertices
            unconnected = self.minKey(key, mstSet)  # call minKey; minKey returns unconnected (index of unreached node)
            mstSet[unconnected] = True  # mstSet at index of node is set to True
            for v_idx in range(self.V_num):  # go through all vertices
                if self.graph[unconnected][v_idx] and not mstSet[v_idx] \
                        and key[v_idx] > self.graph[unconnected][v_idx]:
                    key[v_idx] = self.graph[unconnected][v_idx]
                    # if edge from u to connected node v is > 0 (if there is an edge)
                    #and mstSet[v] is unreached
                    #and key[v] is greater than the edge cost
                    # (only if the current edge cost is greater will need to change)
                    # key[v] takes edge cost

                    mst_edges[v_idx] = unconnected  # mst_edges[v] is index of node; so list of mst_edgess (nodes) is the MST

        self.printMST(mst_edges)  # print the list of mst_edgess, i.e. the MST


def main():
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.primMST()


if __name__ == "__main__":
    main()