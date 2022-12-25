aEdges = [['w', 'x'], ['x', 'y'], ['z', 'y'], ['z', 'v'], ['w', 'v']]


def buildGraph(edges):
    """
    HELPER FUNCTION.
    Builds an undirected graph from a 2D list of edges
    """
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = dict({nodeA: True})
    queue = [(nodeA, 0)]

    while len(queue) > 0:
        node, distance = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if visited.get(neighbor) is None:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    return -1  # no path exists


print(shortestPath(aEdges, 'w', 'z'))  # answer is 2
