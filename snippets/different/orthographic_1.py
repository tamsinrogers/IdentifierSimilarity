def function(t):
    a = ""
    for u in t:
        if u.isalpha():
            # get ascii value of b
            x = ord(u)
            x -= 32
            # convert ascii number to char
            z = chr(x)
            a += z
        else:
            a += u

    return a
