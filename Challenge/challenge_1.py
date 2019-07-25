#!python

"""
Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from sys import argv


class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex
        self.neighbors = {}

    def addNeighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if (vertex not in self.neighbors):
            self.neighbors[vertex] = weight

    def getNeighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def getId(self):
        """return the id of this vertex"""
        return self.id

    def getEdgeWeight(self, vertex):
        """return the weight of this edge"""
        return self.neighbors[vertex]


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vertList = {}
        self.numVertices = 0

    def __str__(self):
        for item in self.vertList:
            print(item)
        return 'done'

    def addVertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex

    def getVertex(self, vertex):
        """return the vertex if it exists"""
        return self.vertList[vertex] if self.vertList[vertex] is not None else False

    def addEdge(self, vertexOne, vertexTwo, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """

        if not vertexOne in self.vertList:
            self.addVertex(vertexOne)
        if not vertexTwo in self.vertList:
            self.addVertex(vertexTwo)

        self.vertList[vertexOne].addNeighbor(
            self.vertList[vertexTwo], cost)

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


if __name__ == "__main__":

    def parse_data():
        '''Takes a text file and turns the information into an array -> list'''
        vertices = open(argv[1], 'r')
        graph_data = vertices.read().split()
        vertices.close()
        return graph_data

    def create_graph(graph_data):
        '''Create a graph from an array of graph information'''
        is_graph = graph_data[0] is 'G'

        graph = Graph()

        for vertex in graph_data[1].split(','):
            graph.addVertex(vertex)

        counter = 0

        for word in graph_data[2:]:
            counter += 1
            if is_graph:
                graph.addEdge(word[3], word[1],
                              word[5:].replace(')', ''))
                graph.addEdge(word[1], word[3],
                              word[5:].replace(')', ''))
            else:
                graph.addEdge(word[1], word[3],
                              word[5:].replace(')', ''))

        return graph, counter

    def print_graph(graph, counter):
        print("# Vertices:", len(graph.getVertices()))
        print("# Edges: ", counter, "\n")
        print("Edge List:")
        for v in graph:
            for w in v.neighbors:
                print("(%s ,%s, %s)" %
                      (v.getId(), w.getId(), v.getEdgeWeight(w)))

    graph_data = parse_data()
    graph, counter = create_graph(graph_data)
    print_graph(graph, counter)
