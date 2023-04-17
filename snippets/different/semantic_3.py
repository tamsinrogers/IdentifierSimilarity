def function(a, b):
    c = []
    for x in a:
        for y in x:
            t = False
            if y in b:
                t = True
            if x in b:
                t = False
            if t:
                c.append(y)
    return c
