file = open('input.txt')
n, m = [int(x) for x in file.readline().split()]
matrix = [[0] * n for _ in range(n)]

W = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in file.readline().split()]
    u -= 1
    v -= 1
    W[u].append(v)

for i in range(n):
    for vertex in W[i]:
        matrix[i][vertex] = 1

for line in matrix:
    print(*line)
