from heapq import *

n = int(input())
costs = [int(x) for x in input().split()]
W = [[0] * n for _ in range(n)]

m = int(input())  # количество дорог
for i in range(m):
    line = input()
    u, v = [int(x) - 1 for x in line.split()]
    W[u][v] = costs[u]
    W[v][u] = costs[v]

INF = float('inf')
start = 0
visited = [False] * n
dist = [INF] * n
dist[start] = 0

h = [(0, start)]
heapify(h)

while h:
    cur_dist, u = heappop(h)
    if visited[u]:
        continue
    for v in range(n):
        if W[u][v] != 0 and not visited[v]:
            if dist[u] + W[u][v] < dist[v]:
                dist[v] = dist[u] + W[u][v]
                heappush(h, (dist[u] + W[u][v], v))
    visited[u] = True


if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])