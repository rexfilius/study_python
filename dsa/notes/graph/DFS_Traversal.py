# DFS TRAVERSAL
# DFS explores one direction as far as possible before
# switching directions.
def dfsGraph(graph, start):
    """
    Depth First Search traversal in a graph, whether directed/undirected.
    :param graph: the graph object to be traversed.
    :param start: the node/vertex to start the traversal from.
    """
    visited = dict()
    stack = [start]
    while len(stack) > 0:
        current = stack.pop()
        if visited.get(current) is not True:
            visited[current] = True
            print(current, end='')
        for neighbor in graph[current]:
            if visited.get(neighbor) is not True:
                stack.append(neighbor)


def dfsGraphRecursive(graph, start, visited=None):
    if visited is None:
        visited = dict()
    visited[start] = True
    print(start, end='')
    for neighbor in graph[start]:
        if visited.get(neighbor) is not True:
            dfsGraphRecursive(graph, neighbor, visited)


def dfsDirected(graph, start):
    """
    DFS traversal in a directed graph.
    """
    stack = [start]
    while len(stack) > 0:
        current = stack.pop()
        print(current, end='')
        for neighbor in graph[current]:
            stack.append(neighbor)


def dfsDirectedRecursive(graph, source):
    """
    A base case for this recursion is when a node has no neighbour.
    """
    print(source, end='')
    for neighbor in graph[source]:
        dfsDirectedRecursive(graph, neighbor)
