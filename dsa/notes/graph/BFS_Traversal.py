# BFS TRAVERSAL.
# BFS explores all direction evenly, instead of favoring one all
# the way through. BFS is iterative only, no recursion.

def bfsGraph(graph, start):
    """
    Breadth First Search traversal in a graph, whether directed/undirected.
    :param graph: the graph object to be traversed.
    :param start: the node/vertex to start the traversal from.
    """
    visited = dict()
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        if visited.get(current) is not True:
            visited[current] = True
            print(current, end='')
        for neighbor in graph[current]:
            if visited.get(neighbor) is not True:
                queue.append(neighbor)


def bfsDirected(graph, start):
    """
    BFS traversal in a directed graph.
    """
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current, end='')
        for neighbour in graph[current]:
            queue.append(neighbour)
