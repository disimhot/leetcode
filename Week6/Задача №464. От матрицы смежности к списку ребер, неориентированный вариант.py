file = open('input.txt')
n = int(file.readline())
V = dict((i, []) for i in range(1, n + 1))

for i in range(1, n + 1):
    vertices = [int(x) for x in file.readline().split()]
    for j in range(i, n + 1):
        if vertices[j - 1] != 0:
            V[i].append(j)

for key, values in V.items():
    for v in values:
        print(key, v)
