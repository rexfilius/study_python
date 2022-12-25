"""
Write a function that takes in a grid containing W's and L's. W represents Water
and L represents Land. The function should return the size of the smallest island.
An island is a vertically or horizontally connected region of land.
You may assume that the grid contains at least one island.
"""

mGrid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]


def minIslandCount(grid):
    visited = dict()
    minSize = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = exploreGridSize(grid, row, col, visited)
            if 0 < size < minSize:  # size > 0 and size < minSize
                minSize = size
    return minSize


def exploreGridSize(grid, row, col, visited=None):
    if visited is None:
        visited = dict()
    rowInbounds = 0 <= row < len(grid)
    colInbounds = 0 <= col < len(grid[0])
    if not rowInbounds or not colInbounds:
        return 0
    if grid[row][col] == 'W':
        return 0

    pos = f"{row},{col}"  # position on the grid
    if visited.get(pos):
        return 0
    visited[pos] = True

    size = 1
    size += exploreGridSize(grid, row - 1, col, visited)
    size += exploreGridSize(grid, row + 1, col, visited)
    size += exploreGridSize(grid, row, col - 1, visited)
    size += exploreGridSize(grid, row, col + 1, visited)
    return size


print(minIslandCount(mGrid))
