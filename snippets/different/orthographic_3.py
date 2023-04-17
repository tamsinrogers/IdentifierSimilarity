def function(input):
    x = ""
    u = ""
    # for each word in the string
    for j in input.split():
        if j[0] in ["a", "e", "i", "o", "u", "y"]:
            x = x + j + " "
        else:
            u = u + j + " "

    return x, u
