def function(x, index=False):

    max_x = max_i = min_i = 0
    min_x = 1e9

    for i in range(len(x)):
        if x[i] < min_x:
            min_x = x[i]
            min_i = i

        elif x[i] > max_x:
            max_x = x[i]
            max_i = i

    if index:
        return (min_i, max_i)
    else:
        return (min_x, max_x)
