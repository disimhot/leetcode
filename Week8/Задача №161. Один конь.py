N = int(input())
x1, y1 = [int(x) - 1 for x in input().split()]
x2, y2 = [int(x) - 1 for x in input().split()]

V = [[-1] * N for _ in range(N)]
queue = [-1] * (N ^ 2)

queue = [(x1, y1)]
V[x1][y1] = 0
trace = {}


def possible_moves(x, y):
    moves = [(x - 1, y - 2),
             (x - 2, y - 1),
             (x - 2, y + 1),
             (x - 1, y + 2),
             (x + 1, y + 2),
             (x + 2, y + 1),
             (x + 2, y - 1),
             (x + 1, y - 2)]
    return [(x, y) for x, y in moves if -1 < x < N and -1 < y < N]


while queue:
    i, j = queue.pop()
    for x, y in possible_moves(i, j):
        if -1 < x < N and -1 < y < N:
            if V[x][y] == -1:
                queue = [(x, y)] + queue
                V[x][y] = V[i][j] + 1
                trace[(x, y)] = (i, j)
            elif x == x2 and y == y2:
                break
        else:
            continue

print(V[x2][y2])
path = [(x2, y2)]

while path[-1] != (x1, y1):
    last_node = path[-1]
    next_node = trace[last_node]
    path.append(next_node)
for x, y in path[::-1]:
    print(x + 1, y + 1)
