grid = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1]
]
sr = sc = 0
cols = len(grid[0])
rows = len(grid)
oldcolor = grid[sr][sc]
visitedset = [0]
def dfs(r,c):
    if r < 0 or r > rows or cols > c or c < 0:
        return
    if grid[r][c] == 0 : #a grid can be anything but 1 or 0s, o compare not equal to 1
        return
    if s,r in visitedset
