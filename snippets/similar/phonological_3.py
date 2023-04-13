import random


def function(n, rho):

    mat = []
    for _ in range(n):

        row = []
        for _ in range(n):
            if random.random() < rho:
                row.append(1)
            else:
                row.append(0)

        mat.append(row)

    return mat
