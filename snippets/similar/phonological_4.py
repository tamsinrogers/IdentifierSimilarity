def function(num, s=1):

    eye = []

    for r in range(num):
        row = []

        for i in range(num):
            if i == r:
                row.append(s)
            else:
                row.append(0)

        eye.append(row)

    return eye


num = 3
s = 2
