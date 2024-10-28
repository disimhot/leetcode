n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = matrix[i][j]
        if matrix[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

ans = sum([sum([x for x in row]) for row in dp])
print(ans)

# 3 4
# 0 1 1 1
# 1 1 1 1
# 0 1 1 1
