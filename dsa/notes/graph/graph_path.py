# this graph is directed and acyclic
gg = {'f': ['g', 'i'], 'g': ['h'], 'h': [], 'i': ['g', 'k'], 'j': ['i'], 'k': []}


def directedPathDFSrecurse(graph, src, dest):
    """
    Checks if there is a path between source node and destination node.
    :return: True, if there's a path, otherwise, false.
    This algo uses dfs(call stack) and recursion
    """
    if src == dest:
        return True
    for neighbour in graph[src]:
        if directedPathDFSrecurse(graph, neighbour, dest) is True:
            return True
    return False


def directedPathDFS(graph, src, dest):
    """
    Checks if there is a path between source node and destination node.
    :return: True, if there's a path, otherwise, false.
    """
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        if current == dest:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False


def directedPathBFS(graph, src, dest):
    """
    Checks if there is a path between source node and destination node.
    :return: True, if there's a path, otherwise, false.
    This algo uses bfs.
    """
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


print(directedPathDFSrecurse(gg, 'f', 'k'))
print(directedPathDFS(gg, 'f', 'k'))
print(directedPathBFS(gg, 'f', 'k'))
