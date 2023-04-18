def function(o):
    # sort the list in ascending order
    o = sorted(o, reverse=False)
    l = len(o)
    i = []
    j = []
    for c in range(l):
        if o[c] % 2 == 0:
            i.append(o[c])
        else:
            j.insert(0, o[c])
    return i, j
