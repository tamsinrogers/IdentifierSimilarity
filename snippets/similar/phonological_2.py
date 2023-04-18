def function(points, square):

    err = 0

    for pair in points:
        y_approx = square(pair[0])
        err += (pair[1] - y_approx)**2

    return err/len(points)
