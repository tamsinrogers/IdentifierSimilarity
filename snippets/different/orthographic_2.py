def function(a):
    # sort the list in ascending order
    a = sorted(a, reverse=False)
    l = len(a)
    u = []
    t = []
    for i in range(l):
        if a[i] % 2 == 0:
            u.append(a[i])
        else:
            t.insert(0, a[i])
    return u, t
