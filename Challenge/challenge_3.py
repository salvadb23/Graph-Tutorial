from challenge_1 import Graph, Vertex
from challenge_2 import create_graph, parse_data


'''Ask soul why are these giving different outputs'''


def rescursive_dfs(graph, v):
    vertexObj = graph.vertList[v]
    result = [vertexObj]
    visited = {}

    def dfs(vertex):
        visited[vertex.getId()] = True
        for neighbor in vertex.neighbors:
            if neighbor not in visited:
                dfs(neighbor)
    dfs(vertexObj)

    return list(visited.keys())


def dfs(graph, v):
    '''An algorithm that returns a path of reachable vertices from an initial vertex'''
    vertexObj = graph.vertList[v]
    stack = [vertexObj]
    visited = {}

    while len(stack):
        vertex = stack.pop()
        visited[vertex.getId()] = True

        for neighbor in vertex.neighbors:
            stack.append(neighbor)

    return list(visited.keys())


graph_data = parse_data()
graph = create_graph(graph_data)[0]
recursive_dfs_result = rescursive_dfs(graph, '1')
result = dfs(graph, '1')
print(result)
print()
