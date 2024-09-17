def generate(numRows: int):
    init = [1]
    A = []
    for i in range(1, numRows + 1):
        A.append(init * i)
    for i in range(2, numRows):
        for j in range(1, len(A[i]) - 1):
            A[i][j] = A[i - 1][j - 1] + A[i - 1][j]

    return A


print(generate(5))
