n = int(input())
dp = [0] * n
a = [[int(x) for x in input().split()] for _ in range(n)]

dp[0] = a[0][0]
if n > 1:
    dp[1] = min(a[0][0] + a[1][0], a[0][1])

for i in range(2, n):
    dp[i] = min(dp[i - 3] + a[i - 2][2],
                dp[i - 2] + a[i - 1][1],
                dp[i - 1] + a[i][0])

print(dp[n - 1])
