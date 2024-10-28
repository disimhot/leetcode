def maxProfit(prices, fee):
    n = len(prices)
    empty = [0] * n  # макс прибыль: продали акцию по prices[i] цене, кот-ю купили ранее, или ничего не делаем
    hold = [0] * n  # купили акцию по prices[i] цене и еще не продали
    hold[0] = -prices[0]

    for i in range(1, n):
        hold[i] = max(hold[i - 1], empty[i - 1] - prices[i])
        empty[i] = max(empty[i - 1], hold[i - 1] + prices[i] - fee)

    return empty[n - 1]


print(maxProfit([2, 1, 4, 4, 2, 3, 2, 5, 1, 2], 1))  # 4
print(maxProfit([1, 4, 6, 2, 8, 3, 10, 14], 3))  # 13
print(maxProfit([9, 8, 7, 1, 2], 3))  # 0
