def mincostTickets(days, costs):
    start = days[0]
    end = days[-1]
    dp = [0] * (end + 1)
    for i in range(start, end + 1):
        if i in days:
            j = min(i, 7)
            k = min(i, 30)
            dp[i] = min(dp[i - 1] + costs[0], dp[i - j] + costs[1], dp[i - k] + costs[2])
        else:
            dp[i] = dp[i - 1]

    return dp[end]


# print(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))  # 11
print(mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))  # 17
