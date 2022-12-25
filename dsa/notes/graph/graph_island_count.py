"""
Write a function that takes in a grid containing W's and L's. W represents water
and L represents Land. The function should return the number of islands on the grid.
An island is a vertically or horizontally connected region of land.
"""
gridGraph = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]


def islandCount(grid):
    visited = dict()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):  # for col in range(len(grid[row]))
            if exploreGrid(grid, row, col, visited):
                count += 1
    return count


def exploreGrid(grid, row, col, visited=None):
    if visited is None:
        visited = dict()
    rowInbounds = 0 <= row < len(grid)
    colInbounds = 0 <= col < len(grid[0])
    if not rowInbounds or not colInbounds:
        return False
    if grid[row][col] == 'W':
        return False

    pos = f"{row},{col}"  # position on the grid
    if visited.get(pos):
        return False
    visited[pos] = True
    exploreGrid(grid, row - 1, col, visited)
    exploreGrid(grid, row + 1, col, visited)
    exploreGrid(grid, row, col - 1, visited)
    exploreGrid(grid, row, col + 1, visited)
    return True


print(islandCount(gridGraph))
