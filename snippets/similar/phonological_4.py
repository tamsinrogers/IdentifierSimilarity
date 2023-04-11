def function(y, index=False):

    max_y = max_i = min_i = 0
    min_y = 1e9

    for i in range(len(y)):
        if y[i] < min_y:
            min_y = y[i]
            min_i = i

        elif y[i] > max_y:
            max_y = y[i]
            max_i = i

    if index:
        return (min_i, max_i)
    else:
        return (min_y, max_y)
