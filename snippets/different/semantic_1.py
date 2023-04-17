def function(a, b):
    i = 0
    while i < len(a):
        print(i)
        if type(a[i]) == str:
            b.append(a[i])
            a.remove(a[i])
        elif type(a[i]) == float:
            b.append("0")
            a.remove(a[i])
        else:
            i += 1
    j = 0
    while j < len(b):
        if type(b[j]) == int:
            a.append(b[j])
            b.remove(b[j])
        elif type(b[j]) == float:
            a.append(0)
            b.remove(b[j])
        else:
            j += 1

    return a, b
