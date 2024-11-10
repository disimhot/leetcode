from copy import deepcopy
from itertools import permutations
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)
        self.n = len(self.matrix)

    def size(self):
        return self.n

    def solve(self, y):
        general_det = self.determinant(self.matrix)
        linear_span = []
        if general_det == 0:
            raise ValueError()
        else:
            for i in range(self.n):
                aux_matrix = deepcopy(self.matrix)
                for j in range(self.n):
                    aux_matrix[j][i] = y[j]
                aux_determinant = self.determinant(aux_matrix)
                dot = aux_determinant / general_det
                linear_span.append(dot)
            return linear_span

    @staticmethod
    def determinant(matrix):
        det = 0
        n = len(matrix)
        perms = permutations([x for x in range(n)])
        for p in perms:
            inversions = 0
            product = 1
            for i in range(n):
                for j in range(i + 1, n):
                    if p[i] > p[j]:
                        inversions += 1
                k = p[i]
                product *= matrix[i][k]
            sgn = 1 if inversions % 2 == 0 else -1
            det += sgn * product
        return det


m = Matrix([[1, 2, -1, 3],
            [2, -1, 3, 1],
            [-1, 4, 2, -1],
            [3, -2, 1, 2]])
print(m.solve([10, 5, 3, 7]))

# Проверка алгоритма
np_matrix = np.array([[1, 2, -1, 3],
                      [2, -1, 3, 1],
                      [-1, 4, 2, -1],
                      [3, -2, 1, 2]])
b = np.array([10, 5, 3, 7])

print(np.linalg.solve(np_matrix, b))
