def function(a):
    b = False
    c = False
    for x in a:
        if len(x) < 5:
            b = True
        else:
            if len(x) < 10:
                c = True
        if b:
            print(x[0])
        elif c:
            print(b)
        else:
            print(x[1])
        b = False
        c = False
