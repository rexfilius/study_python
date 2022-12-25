# An undirected graph
eGraph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

eGraph2 = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}


def largestComponent(graph):
    visited = dict()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size
    return longest


def exploreSize(graph, node, visited=None):
    if visited is None:
        visited = dict()
    if visited.get(node):
        return 0
    visited[node] = 1
    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)
    return size


print(largestComponent(eGraph))
