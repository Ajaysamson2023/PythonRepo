import numpy as np


def linear_algebra():
    n = int(input("Enter value:"))

    arr = []
    for i in range(n):
        arr.append(list(map(float, input("Enter  two values in 2 dimension matrix:").split())))

    matrix = np.matrix(arr)
    result = np.linalg.det(matrix)
    result_1 = round(result, 2)
    print(result_1)
    return result_1
