def rob(nums):
    n = len(nums)
    if n <= 3:
        return max(nums)

    dp_odd = [0] * (n - 1)  # 0 ... n-2
    dp_odd[0] = nums[0]
    dp_odd[1] = max(nums[0], nums[1])

    dp_even = [0] * n  # 1 ... n-1
    dp_even[1] = nums[1]
    dp_even[2] = max(nums[1], nums[2])

    for i in range(2, n):
        if i < n - 1:
            dp_odd[i] = max(dp_odd[i - 1], dp_odd[i - 2] + nums[i])
        dp_even[i] = max(dp_even[i - 1], dp_even[i - 2] + nums[i])
    ans = max(dp_even[-1], dp_odd[-1])
    return ans


# print(rob([1, 2, 3]))  # 3
# print(rob([1, 2, 3, 1]))  # 4
print(rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))  # 16
