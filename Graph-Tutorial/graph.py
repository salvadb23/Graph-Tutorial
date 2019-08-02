#!python

"""
Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from collections import deque


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
            self.addVertex(vertexOne)
        elif self.vertList[vertexTwo] is None:
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

    def degree_BFS(self, vertex, n=0):
        if (self.vertList[vertex]):
            iteration = 0
            vertexObj = self.vertList[vertex]
            queue = deque([(vertexObj, iteration)])
            results = []
            visited = {}
            visited[vertex] = True

            while len(queue):
                (current_element, iteration) = queue.popleft()
                if iteration > n:
                    break
                elif iteration is n:
                    results.append(current_element.id)

                visited[current_element.id] = True
                key = current_element.id
                for neighbor in self.vertList[key].neighbors:
                    if neighbor.id not in visited:
                        visited[neighbor.id] = True
                        queue.append((neighbor, iteration + 1))

            return results

    def BFS(self, vertex):
        vertexObj = self.vertList[vertex]
        queue = deque([vertexObj])
        visited = {}

        visited[vertexObj.id] = True

        while len(queue):
            current_item = queue.popleft()

            for neighbor in current_item.neighbors:
                if neighbor not in visited:
                    visited[vertex] = True
                    queue.append(neighbor)

        return list(visited.keys())

    def find_shortest_path(self, vertex_one, vertex_two):
        '''Finds the shortest path between two vertices'''
        queue = [(vertex_one, 0)]
        visited = {}
        path = []
        while queue:
            if vertex_two in visited:
                break
            vertex, parent = queue.pop(0)
            if len(visited.keys()) is len(self.vertList):
                break
            if vertex not in visited:
                visited[vertex] = parent

            for neighbor in self.vertList[vertex].neighbors:
                if neighbor not in visited:
                    queue.append((neighbor.getId(), vertex))

        child = vertex_two
        while vertex_one not in path:
            path.append(child)
            child = visited[child]
        return path[::-1]

    def clique(self):
        


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.addVertex("Karen")
    g.addVertex("Jordan")
    g.addVertex("Hannah")
    g.addVertex("Zakye")
    g.addVertex("William")
    g.addVertex("Salvador")
    g.addVertex("Dacio")
    g.addVertex("Erika")
    g.addVertex("Deontae")
    g.addVertex('Xavier')

    # Add connections (non weighted edges for now)

    g.addEdge('William', 'Salvador')
    g.addEdge("William", "Karen")
    g.addEdge("William", "Erika")
    g.addEdge("William", "Hannah")
    g.addEdge("William", "Jordan")
    g.addEdge("William", "Hannah")
    g.addEdge("William", "Dacio")
    g.addEdge("William", "Salvador")
    g.addEdge("William", "Xavier")

    g.addEdge("Jordan", "Hannah")
    g.addEdge("Jordan", "Karen")
    g.addEdge("Jordan", "Zakye")
    g.addEdge("Jordan", "Deontae")
    g.addEdge("Jordan", "Xavier")

    g.addEdge("Hannah", 'Erika')
    g.addEdge("Hannah", "Jordan")
    g.addEdge("Hannah", "Karen")
    g.addEdge("Hannah", "Zakye")
    g.addEdge("Hannah", "Deontae")
    g.addEdge("Hannah", "Xavier")

    g.addEdge("Erika", 'Hannah')
    g.addEdge("Erika", "Jordan")
    g.addEdge("Erika", "Karen")
    g.addEdge("Erika", "Zakye")
    g.addEdge("Erika", "Deontae")
    g.addEdge("Erika", "Xavier")

    g.addEdge("Dacio", "Salvador")
    g.addEdge("Dacio", "Erika")

    g.addEdge("Salvador", "Dacio")
    g.addEdge("Salvador", "Erika")

    g.addEdge('Xavier', 'Erika')
    g.addEdge('Xavier', 'Zakye')
    g.addEdge('Xavier', 'Deontae')
    g.addEdge('Xavier', 'Zakye')
    g.addEdge('Xavier', 'Karen')
    g.addEdge('Xavier', 'Hannah')
    g.addEdge('Xavier', 'Jordan')

    g.addVertex('Hannah')
    g.addVertex('Ciara')
    g.addVertex('Kyle')

    g.addEdge('Hannah', 'Ciara')
    g.addEdge('Ciara', 'Kyle')

    result = g.find_shortest_path("William", "Kyle")
    print(result)
