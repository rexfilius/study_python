from dsa_notes.dsa.graph.DFS_Traversal import dfsGraph

# Adjacency-List-style directed graph
cGraph = {'a': ['b', 'c'],
          'b': ['d'],
          'c': ['e'],
          'd': ['f'],
          'e': [],
          'f': []}

# Adjacency-List-style undirected graph
gGraph = {'w': ['x', 'v'],
          'x': ['w', 'y'],
          'y': ['x', 'z'],
          'z': ['y', 'v'],
          'v': ['w', 'z']}

# Adjacency-List-style undirected graph
kGraph = {'a': ['b', 'c', 'd', 'e'],
          'b': ['c', 'a', 'g'],
          'c': ['a', 'b', 'd'],
          'd': ['a', 'c', 'e', 'h'],
          'e': ['f', 'a', 'd'],
          'f': ['g', 'e', 'h'],
          'g': ['f', 'b'],
          'h': ['f', 'd']}

print(' :: DFS in a directed graph.', dfsGraph(cGraph, 'a'))
print()
print(' :: DFS in an undirected graph.', dfsGraph(gGraph, 'w'))
print()
print(' :: DFS in an undirected graph.', dfsGraph(kGraph, 'a'))
print()