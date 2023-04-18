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


input = "the inclination angle of some galaxy will affect the component of the"
