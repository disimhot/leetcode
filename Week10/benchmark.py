from heapq import *
import time
import random

import random


def generate_dijkstra_input_format(n, density=0.3, max_weight=10000):
    """
    Генерирует граф в формате матрицы смежности с весами путей.
    :param n: количество вершин
    :param density: плотность графа (доля существующих рёбер от всех возможных)
    :param max_weight: максимальный вес рёбер
    :return: список строк, представляющих граф
    """
    matrix = [[0 if i == j else (random.randint(1, max_weight) if random.random() < density else 0)
               for j in range(n)] for i in range(n)]

    # Симметричность графа (для неориентированного графа)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i] = matrix[i][j]

    return matrix




def deikstra(n, W):
    INF = float('inf')
    start = 0
    visited = [False] * n
    dist = [INF] * n # dist[i] - мин. расстояние от start do i
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
    return dist

def deikstra2(n, W):
    INF = float('inf')
    visited = [False] * n
    dist = [INF] * n # dist[i] - мин. расстояние от start do i
    dist[0] = 0

    def gofrom():
        index = 0
        distmin = INF
        for i in range(n):
            if dist[i] < distmin and not visited[i]:
                distmin = dist[i]
                index = i
        return index

    while False in visited:
        u = gofrom()
        for v in range(n):
            if W[u][v] != 0 and not visited[v]:
                dist[v] = min(dist[v], dist[u] + W[u][v])
        visited[u] = True
    return dist

def benchmark(func):
    params = {
        'n': [10000, 10000, 5000, 1000],
        'density': [0.1, 0.5, 0.9, 1],
    }
    results = []
    for n, d in zip(params['n'], params['density']):
        W = generate_dijkstra_input_format(n, d)
        start = time.time()
        func(n, W)
        end = time.time()
        print(n, d, end - start)
        results.append(end - start)
    return results

# print('time for heap deikstra:', benchmark(deikstra))
# 10000 0.1 5.583 - разреженные графы
# 10000 0.5 10.019 - разреженные графы
# 5000 0.9 3.585 - полные графы
# 1000 1 0.144 - полные графы

print('time for simple deikstra:', benchmark(deikstra2))

# 10000 0.1 10.362 - разреженные графы
# 10000 0.5 16.009 - разреженные графы
# 5000 0.9 5.495 - полные графы
# 1000 1 0.23 - полные графы