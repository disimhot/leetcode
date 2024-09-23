def binary_search(a, x):
    l = 0
    h = len(a)
    while l < h:
        c = (l + h) // 2
        if a[c] < x:
            l = c + 1
        elif a[c] > x:
            h = c
        else:
            return c
    return -1


def findContentChildren(g, s):
    if len(s) == 0:
        return 0
    g = sorted(g)
    s = sorted(s)
    count = 0
    j = 0
    for i in range(len(s)):
        if s[i] >= g[j]:
            count += 1
            j += 1
        if j == len(g):
            break

    return count


# print(findContentChildren([1, 2, 3], [2, 3]))
# print(findContentChildren([1, 2, 3], [3]))
# print(findContentChildren([1, 2], [1, 2, 3]))
print(findContentChildren([9, 7, 7, 10], [5, 6, 7, 8]))
