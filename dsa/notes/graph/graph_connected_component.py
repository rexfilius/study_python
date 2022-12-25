# An Undirected Graph
dGraph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}

# An undirected graph
dGraph2 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def connectedComponentCount(graph):
    """
    :return: the number of connected component within the graph
    """
    visited = dict()
    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, currentNode, visited=None):
    if visited is None:
        visited = dict()
    if visited.get(currentNode):
        return False
    visited[currentNode] = True
    for neighbor in graph[currentNode]:
        explore(graph, neighbor, visited)
    return True


print(connectedComponentCount(dGraph2))
