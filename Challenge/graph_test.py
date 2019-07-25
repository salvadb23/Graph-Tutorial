from challenge_1 import Graph, Vertex
import unittest


class VertextTest(unittest.TestCase):

    def test_vertex_init(self):
        vertex = Vertex('A')
        assert vertex.getId() is 'A'
        assert len(vertex.getNeighbors()) is 0

    def test_neighbors(self):
        vertex = Vertex('A')
        vertex_two = Vertex('B')
        vertex.addNeighbor(vertex_two, 10)
        assert len(vertex.getNeighbors()) is 1
        assert vertex.getEdgeWeight(vertex_two) is 10


class GraphTest(unittest.TestCase):

    def test_init(self):
        graph = Graph()
        assert len(graph.vertList) is 0
        assert graph.numVertices is 0

    def test_add_vertex(self):
        graph = Graph()
        lst = ["A", "B", "C", "D"]
        [graph.addVertex(vert) for vert in lst]
        assert len(graph.vertList) is 4
        assert graph.numVertices is 4
        assert graph.getVertex('A').getId() is 'A'
        assert graph.getVertex('B').getId() is 'B'

    def test_add_edge(self):
        graph = Graph()
        lst = ["A", "B", "C", "D"]
        [graph.addVertex(vert) for vert in lst]
        graph.addEdge('A', 'B')
