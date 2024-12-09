# https://www.algoexpert.io/questions/river-sizes
def riverSizes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rivers = []

    def dfs(i, j):
        if (-1 < i < n and -1 < j < m) and matrix[i][j] == 1:
            size = 1
            matrix[i][j] = 0
            size += dfs(i + 1, j)
            size += dfs(i - 1, j)
            size += dfs(i, j + 1)
            size += dfs(i, j - 1)
            return size
        return 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                size = dfs(i, j)
                if size > 0:
                    rivers.append(size)
    return sorted(rivers)


print(riverSizes(
    [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
))
