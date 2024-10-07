N, k = [int(x) for x in input().split()]
s, *stations = [int(x) for x in input().split()]
count = 0
cur = k

if cur < N:
    stations.append(N)
    for i in range(s + 1):
        if stations[i] > cur:
            count = -1
            break
        else:
            if i == s:
                break
            if cur - stations[i + 1] < 0:
                count += 1
                cur += k

print(count)

# 100 20
# 3 20 40 60
#
# 100 20
# 4 20 40 60 80

# 100 60
# 3 10 20 80
