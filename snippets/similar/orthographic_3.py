def function(m):
    u = ""
    n = ""
    for v in m.split():
        if v[0] in ["a", "e", "i", "o", "u", "y"]:
            u = u + v + " "
        else:
            n = n + v + " "

    return u, n
