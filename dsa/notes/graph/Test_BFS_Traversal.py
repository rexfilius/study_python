from dsa_notes.dsa.graph.BFS_Traversal import bfsGraph

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

print(' :: BFS in a directed graph.', bfsGraph(cGraph, 'a'))
print()
print(' :: BFS in an undirected graph.', bfsGraph(gGraph, 'w'))
print()
print(' :: BFS in an undirected graph.', bfsGraph(kGraph, 'a'))
print()
