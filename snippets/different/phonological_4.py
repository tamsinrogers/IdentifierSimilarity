def function(n, s=1):

    eye = []

    for r in range(n):
        row = []

        for c in range(n):
            if c == r:
                row.append(s)
            else:
                row.append(0)

        eye.append(row)

    return eye


n = 3
s = 2
