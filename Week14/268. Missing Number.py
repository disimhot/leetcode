def missingNumber(nums):
    n = len(nums)
    sum = (n + 1) * n // 2
    for a in nums:
        sum -= a
    return sum
print(missingNumber([3, 0, 1]))