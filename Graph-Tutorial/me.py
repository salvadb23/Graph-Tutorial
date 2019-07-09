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

    def __str__(self):
        """output the list of neighbors of this vertex"""
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

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
        if self.vertList[vertexOne] is None:
          # TODO: THese return vertexes they do not add
            self.addVertex(vertexTwo)
        elif self.vertList[vertexTwo] is None:
           # TODO: THese return vertexes they do not add to vert list
            self.addVertex(vertexTwo)
        else:
            self.vertList[vertexOne].addNeighbor(self.vertList[vertexTwo])
            self.vertList[vertexTwo].addNeighbor(self.vertList[vertexOne])

    def getVertices(self):
        """return all the vertices in the graph"""
        return self.vertList.keys()

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertList.values())


'''
will = Vertex('William')
zakye = Vertex("Zakye")
deontae = Vertex("Deontae")
will.addNeighbor(zakye)
will.addNeighbor(deontae)
print(will.neighbors[zakye])
'''

g = Graph()
g.addVertex("Karen")
g.addVertex("Jordan")
g.addVertex("William")

g.addEdge('Karen', 'William')
g.addEdge('William', 'Jordan')

print(g)
