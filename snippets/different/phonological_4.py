def function(x, index=False):

    var = num = integer = 0
    min_x = 1e9

    for i in range(len(x)):
        if x[i] < min_x:
            min_x = x[i]
            integer = i

        elif x[i] > var:
            var = x[i]
            num = i

    if index:
        return (integer, num)
    else:
        return (min_x, var)
