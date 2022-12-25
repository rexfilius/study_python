edges_ = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]
# convert this edges to adjacency list, you now have an Undirected Graph
graph_ = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'l': ['k'],
    'm': ['k'],
    'n': ['o'],
    'o': ['n']
}


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


def undirectedPathDFS(edges, nodeA, nodeB):
    """
    Checks if there is a path between two nodes in an undirected graph.
    :return: True, if there's a path, otherwise, false.
    This algo uses dfs(call stack) and recursion
    """
    graph = buildGraph(edges)
    return hasPathDFS(graph, nodeA, nodeB, visited=dict())


def hasPathDFS(graph, src, dest, visited=None):
    if visited is None:
        visited = dict()
    if src == dest:
        return True
    if visited.get(src):
        return False
    visited[src] = True
    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dest, visited) is True:
            return True
    return False


# print(buildGraph(edges_))
print(undirectedPathDFS(edges_, 'i', 'l'))
