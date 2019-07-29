from challenge_1 import Graph, Vertex, create_graph, parse_data
from sys import argv

'''Ask soul why are these giving different outputs'''


def DFS_recursive(self, v, v2):
    """searches the graph to see if there is a path between two vertices using DFS"""
    vertexObj = self.vertList[v]
    visited = {}
    visited[vertexObj.getId()] = True

    def dfs(vertex):
        visited[vertex.getId()] = True
        for neighbor in vertex.neighbors:
            if neighbor.getId() not in visited:
                dfs(neighbor)

    dfs(vertexObj)

    path = list(visited.keys())
    end_path = path.index(v2) + 1

    is_path = v2 in path

    return (is_path, path[:end_path])


def print_path_result(path, path_list):
    print("There exist a path between vertex {} and {}: {}".format(
        argv[2], argv[3], path))
    print('Vertices in path: {}'.format((',').join(path_list)))


graph_data = parse_data()
graph = create_graph(graph_data)[0]
path, path_list = DFS_recursive(graph, '1', '5')
print_path_result(path, path_list)
