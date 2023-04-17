def function(t):
    x = ""
    u = ""
    # for each word in the string
    for z in t.split():
        if z[0] in ["a", "e", "i", "o", "u", "y"]:
            x = x + z + " "
        else:
            u = u + z + " "

    return x, u
