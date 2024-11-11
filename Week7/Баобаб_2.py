# # Проверка, что граф является деревом
# # Должны выполняться два условия: граф должен быть связным и число ребер = число вершин - 1
file = open('input.txt')
n = int(file.readline())
V = [[] for _ in range(n)]
m = 0
for i in range(n):
    vertices = [int(x) for x in file.readline().split()]
    for j in range(i, n):
        if vertices[j] != 0:
            V[i].append(j)
            V[j].append(i)
            m += 1

visited = [False] * n
ncomp = 0


def dfs(start):
    visited[start] = True
    for u in V[start]:
        if not visited[u]:
            dfs(u)


for i in range(n):
    if not visited[i]:
        ncomp += 1
        dfs(i)

if ncomp > 1 or (n - 1 != m):
    print('NO')
else:
    print('YES')
