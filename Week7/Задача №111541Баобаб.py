# # Проверка, что граф является деревом
# # Должны выполняться два условия: граф должен быть связным и число ребер = число вершин - 1

n = int(input())
V = [[int(x) for x in input().split()] for _ in range(n)]
m = 0

for i in range(n):
    for j in range(i, n):
        if V[i][j] == 1:
            m += 1

visited = [False] * n
ncomp = 0


def dfs(start):
    visited[start] = True
    for i in range(n):
        if not visited[i] and V[start][i] != 0:
            dfs(i)


for i in range(n):
    if not visited[i]:
        ncomp += 1
        dfs(i)

if ncomp > 1 or (n - 1 != m):
    print('NO')
else:
    print('YES')
