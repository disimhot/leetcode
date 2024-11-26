def numIslands(grid):
  def dfs(i, j):
    if (-1 < i < n and -1 < j < m) and grid[i][j] == "1":
      grid[i][j] = "0"
      dfs(i+1, j)
      dfs(i-1, j)
      dfs(i, j+1)
      dfs(i, j-1)

  nisland = 0
  n = len(grid)
  m = len(grid[0])
  for i in range(n):
    for j in range(m):
      if grid[i][j] == "1":
        nisland += 1
        dfs(i, j)
  return nisland


print(numIslands(
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
))
