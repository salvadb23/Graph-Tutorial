from challenge_1 import Graph, Vertex, create_graph, parse_data, print_graph
from sys import argv


def has_Eularian_Cycle(graph):
    '''Test if a graph has an Eularian cycle i.e 
    returns True or False
    '''
    for vertex in graph.vertList:
        if len(graph.vertList[vertex].getNeighbors()) % 2 != 0:
            return False
    return True


if __name__ == "__main__":
    graph_data = parse_data()
    graph, counter = create_graph(graph_data)
    x = has_Eularian_Cycle(graph)
    print(x)
