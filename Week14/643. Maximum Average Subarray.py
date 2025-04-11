import math


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    l = len(nums)
    if l == 1:
        return nums[0]

    curSum = sum(nums[0:k])
    maxSum = curSum

    for i in range(1, l - k + 1):
        curSum = curSum - nums[i - 1] + nums[i + k - 1]

        if curSum > maxSum:
            maxSum = curSum

    return maxSum / k


print(findMaxAverage([4,0,4,3,3], 5))
# print(findMaxAverage([5], 1))
