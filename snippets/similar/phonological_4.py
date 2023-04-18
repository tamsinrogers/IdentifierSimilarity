def function(n, s=1):

    eye = []

    for r in range(n):
        row = []

        for i in range(n):
            if i == r:
                row.append(s)
            else:
                row.append(0)

        eye.append(row)

    return eye
