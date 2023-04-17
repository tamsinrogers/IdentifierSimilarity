def function(points, square):

    err = 0

    for pair in points:
        y_approx = square(pair[0])
        err += (pair[1] - y_approx)**2

    return err/len(points)


points = [(0, 0), (1, 1/2), (3, 4.5)]


def f(x): return 0.5*x**2


print(function(points, f))
