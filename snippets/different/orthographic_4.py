def function(a, b):
    l = len(a)
    u = 0
    m = 1e9
    c = ""
    x = ""
    for i in range(l):
        k = len(b[i])
        r = 0
        for j in range(k):
            if b[i][j] == 1:
                r += 1
        if r > u:
            c = a[i]
            u = r
        if r < m:
            x = a[i]
            m = r

    return c, x
