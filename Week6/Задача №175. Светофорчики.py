file = open('input.txt')
n, m = [int(x) for x in file.readline().split()]
W = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = [int(x) for x in file.readline().split()]
    W[u].append(v)
    W[v].append(u)

print(*[len(a) for i, a in enumerate(W) if i > 0])
