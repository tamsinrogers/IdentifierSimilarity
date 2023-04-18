def function(input):
    n = ""
    u = ""
    # for each word in the string
    for elem in input.split():
        if elem[0] in ["a", "e", "i", "o", "u", "y"]:
            n = n + elem + " "
        else:
            u = u + elem + " "

    return n, u
