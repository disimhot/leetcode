n, m = [int(x) for x in input().split()]
L = [[int(x) for x in input().split()] for _ in range(n)]

start = (0, 0)
distances =[[0] * m for _ in range(n)]
distances[0][0] = 1
queue = [start]
result_steps = 0
# print('L', L)
def right(i, j):
    for k in range(j, m):
        if L[i][k] == 1:
            return k - 1
        elif L[i][k] == 2:
            global queue, result_steps
            queue = []
            result_steps = distances[i][j]
            # print('RESULT right', result_steps)
            break
    return m - 1


def left(i, j):
    # print('left i, j', i, j)
    for k in range(j, -1, -1):
        if L[i][k] == 1:
            return k + 1
        elif L[i][k] == 2:
            global queue, result_steps
            queue = []
            result_steps = distances[i][j]
            # print('RESULT left', result_steps)
            break
    return 0


def up(i, j):
    for k in range(i, -1, -1):
        if L[k][j] == 1:
            return k + 1
        elif L[k][j] == 2:
            global queue, result_steps
            queue = []
            result_steps = distances[i][j]
            break
    return 0


def down(i, j):
    for k in range(i, n):
        if L[k][j] == 1:
            return k - 1
        elif L[k][j] == 2:
            global queue, result_steps
            queue = []
            result_steps = distances[i][j]
            # print('RESULT down', result_steps)
            break
    return n - 1


def possible_moves(i, j):
    moves = [
        (i, right(i, j)),
        (i, left(i, j)),
        (down(i, j), j),
        (up(i, j), j)
    ]
    return [(x, y) for x, y in moves if x is not None and y is not None]


while queue:
    i, j = queue.pop()
    for x, y in possible_moves(i, j):
        if result_steps != 0:
            break
        if distances[x][y] == 0 and L[x][y] != 1:
            distances[x][y] = distances[i][j] + 1
            queue = [(x, y)] + queue

print(result_steps)
# 3 5
# 0 0 0 0 0
# 0 0 0 1 1
# 1 1 0 0 2

# 4 5
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 1 1 0 0 2


# 4 5
# 0 1 0 1 1
# 0 0 1 0 2
# 0 0 0 0 0
# 1 0 1 0 0

# 5 3
# 0 1 0
# 0 1 0
# 0 0 0
# 1 1 0
# 2 0 0
