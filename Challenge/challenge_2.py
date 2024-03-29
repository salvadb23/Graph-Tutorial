#!python

"""
Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from sys import argv
from collections import deque
from challenge_1 import Graph, Vertex


if __name__ == "__main__":

    def parse_data():
        vertices = open(argv[1], 'r')
        graph_data = vertices.read().split()
        vertices.close()
        return graph_data

    def create_graph(graph_data):
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

    def shortest_path(graph):
        vertexOne = argv[2]
        vertexTwo = argv[3]
        queue = deque([vertexOne])
        visited = {}
        visited[vertexOne] = True

        while len(queue):
            current_element = queue.popleft()

            visited[current_element] = True
            for neighbor in graph.vertList[current_element].neighbors:
                if neighbor.getId() is vertexTwo:
                    visited[vertexTwo] = True
                    return visited
                if neighbor.getId() not in visited:
                    queue.append((neighbor.getId()))
        return visited

    def print_shortest_path(graph):
        path = shortest_path(graph)
        for key in path.keys():
            print(key, end=',')
        print('\nNumber of edges in shortest path: {}'.format(len(path)-1))

    graph_data = parse_data()
    graph, counter = create_graph(graph_data)
    print_shortest_path(graph)
