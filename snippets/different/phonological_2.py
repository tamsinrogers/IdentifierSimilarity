def function(points, func):

    err = 0

    for xy_pair in points:
        y_approx = func(xy_pair[0])
        err += (xy_pair[1] - y_approx)**2

    return err/len(points)
