n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = dp[i][j - 1] + matrix[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + matrix[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
print(dp[-1][-1])
