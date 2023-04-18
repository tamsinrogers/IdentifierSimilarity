import random


def function(n, den):

    mat = []
    for _ in range(n):

        row = []
        for _ in range(n):
            if random.random() < den:
                row.append(1)
            else:
                row.append(0)

        mat.append(row)

    return mat


n = 3
den = 0.5
