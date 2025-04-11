def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for n in nums:
    # побитовый XOR, все повторяющиеся дважды занулятся
        res ^= n
    return res

print(6^6)
