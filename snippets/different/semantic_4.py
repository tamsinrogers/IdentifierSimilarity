def function(a):
    l = len(a)
    i = 0
    b = False
    c = False
    x = True
    y = False
    while i < l:
        if a[i] != 0 and x == True:
            c = True
        elif a[i] == 0 and x == True:
            print(a[i])
        elif a[i] != 0 and b == True:
            print(a[i])
        elif a[i] == 0 and b == True:
            y = True

        if y:
            x = True
            b = False
            c = False
            y = False
        if c:
            b = True
            x = False
            c = False
            y = False

        i += 1
