from heapq import *

N, S, F = [int(x) for x in input().split()]
start, finish = S - 1, F - 1
W = [[int(x) for x in input().split()] for _ in range(N)]


dist = [float('inf')] * N
INF = float('inf')
dist = [INF] * N
dist[start] = 0
h = [(0, start)]
heapify(h)
trace = {}

while h:
    cur_dist, u = heappop(h)
    for v in range(N):
        if W[u][v] != -1:
            if dist[v] > dist[u] + W[u][v]:
                dist[v] = dist[u] + W[u][v]
                heappush(h, (dist[u] + W[u][v], v))
                trace[v] = u

if dist[finish] == INF:
    print(-1)
else:
    path = [finish]
    while path[-1] != start:
        last_node = path[-1]
        next_node = trace[last_node]
        path.append(next_node)
    print(*[x + 1 for x in path[::-1]])


# 3 1 2
# 0 -1 2
# 3 0 -1
# -1 4 0