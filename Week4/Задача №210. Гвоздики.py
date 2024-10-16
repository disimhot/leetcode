# 2 ≤ 𝑁 ≤ 100
n = int(input())
a = sorted([int(x) for x in input().split()])
dp = [0] * n
dp[1] = a[1] - a[0]

if n >= 3:
    dp[2] = a[2] - a[0]
for i in range(3, n):
    dp[i] = min(dp[i - 2] + a[i] - a[i - 1], dp[i - 1] + a[i] - a[i - 1])

print(dp[n - 1])

# 5
# 0 2 4 10 12
