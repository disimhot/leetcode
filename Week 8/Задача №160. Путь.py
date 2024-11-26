# @codeium-disable
N = int(input())
V = [[] for _ in range(N)]

for i in range(N):
    vertices = [int(x) for x in input().split()]
    for j in range(0, N):
        if vertices[j] != 0:
            V[i].append(j)

start, end = [int(x) - 1  for x in input().split()]
queue = [start]
dist = [-1] * N
trace = {}
dist[start] = 0

while queue:
    u = queue.pop()
    for v in V[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue = [v] + queue
            trace[v] = u
            print('trace[v]', trace)
print(trace)
if start == end:
    print(0)
elif dist[end] == -1:
    print(-1)
else:
    path = [end]
    while path[-1] != start:
        last_node = path[-1]
        next_node = trace[last_node]
        path.append(next_node)
    print(dist[end])
    print(*[x + 1 for x in path[::-1]])



# 5
# 0 1 0 0 1
# 1 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 0 0 0
# 3 5