def count_prefixes(a):
    count = 0
    prefix_sum = 0
    max = 0
    all_sum = 0
    for i in range(len(a)):
        all_sum += a[i]
        if a[i] > max:
            max = a[i]
        if i == 0:
            if max == prefix_sum:
                count += 1
        else:
            prefix_sum = all_sum - max
            if max == prefix_sum:
                count += 1
    return count


t = int(input())
for i in range(t):
    n = int(input())
    print(count_prefixes([int(x) for x in input().split()]))

# 1
# 7
# 1 1 0 3 5 2 12

# 1
# 0
# 3
# 3
# 4
# 1
# 2
