def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    n = len(nums)
    prefix_sum = {0: 1}
    current_sum = 0
    for i in range(n):
        current_sum += nums[i]
        if prefix_sum.get(current_sum - k) is not None:
            count += prefix_sum.get(current_sum - k)

        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    return count



print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3)) #2
# Time Limit Exceeded
# count = 0
# n = len(nums)
# prefix_sum = {}
# prefix_sum[0] = 1
# sum = 0
# for i in range(n):
#     sum += nums[i]
#     if sum - k in prefix_sum:
#         count += prefix_sum[sum - k]
#     if sum in prefix_sum:
#         prefix_sum[sum] += 1
#     else:
#         prefix_sum[sum] = 1
# return count
