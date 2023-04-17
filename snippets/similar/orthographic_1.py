def function(p):
    q = ""
    for b in p:
        if b.isalpha():
            # get ascii value of b
            g = ord(b)
            g -= 32
            # convert ascii number to char
            d = chr(g)
            q += d
        else:
            q += b

    return q
