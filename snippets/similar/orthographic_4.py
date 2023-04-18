def function(z, s):
    l = len(z)
    q = 0
    p = 1e9
    b = ""
    d = ""
    for i in range(l):
        f = len(s[i])
        g = 0
        for j in range(f):
            if s[i][j] == 1:
                g += 1
        if g > q:
            b = z[i]
            q = g
        if g < p:
            d = z[i]
            p = g

    return b, d
