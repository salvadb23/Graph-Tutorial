from challenge_1 import Graph, Vertex, create_graph, parse_data


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


graph_data = parse_data()
graph = create_graph(graph_data)[0]
result = rescursive_dfs(graph, '1')
print(result)
